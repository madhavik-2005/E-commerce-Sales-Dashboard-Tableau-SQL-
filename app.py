import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# DB connection
engine = create_engine('postgresql://postgres:Maha#1415@localhost:5432/ecommerce', future=True)

# Page config
st.set_page_config(page_title="E-Commerce Sales Dashboard", layout="wide")

# ----- CSS for colors, alignment, spacing -----
st.markdown("""
<style>
.stApp { background: linear-gradient(180deg, #f7fbff 0%, #ffffff 100%); }
.main-title { text-align: center; color: #2E86C1; font-size: 42px; font-weight: 700; margin-bottom: 30px; }
.kpi-card {
    background: linear-gradient(90deg, rgba(46,134,193,0.12), rgba(46,134,193,0.04));
    border-radius: 12px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 2px 12px rgba(46,134,193,0.08);
    margin-bottom: 20px;
}
.kpi-value { font-size: 24px; font-weight: 700; color: #1f3b6f; }
.kpi-label { font-size: 14px; color: #4b5563; margin-top: 6px; }
.subheader-green { color: #2E8B57; margin-bottom: 8px; }
.subheader-blue { color: #2E86C1; margin-bottom: 8px; }
.subheader-orange { color: #FF8C42; margin-bottom: 8px; }
.section-box {
    padding: 12px 15px;
    border-radius: 10px;
    background: rgba(255,255,255,0.85);
    border: 1px solid rgba(0,0,0,0.05);
    margin-bottom: 20px;
}
.stDataFrame table { width: 100%; border-collapse: collapse; }
.chart-container { margin-top: 20px; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

# MAIN HEADING
st.markdown("<h1 class='main-title'>E-Commerce Sales Dashboard</h1>", unsafe_allow_html=True)

# Helper to check if table/view exists
def exists(name):
    q = text("""
        SELECT EXISTS (
            SELECT 1 FROM information_schema.tables 
            WHERE table_schema = 'public' AND table_name = :name
        ) OR EXISTS (
            SELECT 1 FROM information_schema.views 
            WHERE table_schema = 'public' AND table_name = :name
        )
    """)
    with engine.connect() as conn:
        result = conn.execute(q, {"name": name})
        val = result.scalar()
    return bool(val)

# 1) KPI cards horizontally
try:
    total_sales = pd.read_sql("SELECT SUM(sales) AS total_sales FROM sales", engine).iloc[0,0] or 0
    total_profit = pd.read_sql("SELECT SUM(profit) AS total_profit FROM sales", engine).iloc[0,0] or 0
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<div class='kpi-card'><div class='kpi-value'>${total_sales:,.2f}</div><div class='kpi-label'>Total Sales</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='kpi-card'><div class='kpi-value' style='color:#2E8B57;'>${total_profit:,.2f}</div><div class='kpi-label'>Total Profit</div></div>", unsafe_allow_html=True)
except Exception as e:
    st.error(f"Error loading KPI data: {e}")

# 2) Top entities horizontally
entity_col = None
try:
    with engine.connect() as conn:
        rows = conn.execute(text("SELECT column_name FROM information_schema.columns WHERE table_name='sales' ORDER BY ordinal_position")).all()
    cols = [r[0] for r in rows]
    for candidate in ("customer_name", "customer_id", "country", "region"):
        if candidate in cols:
            entity_col = candidate
            break
except Exception as e:
    st.error(f"Error reading sales table schema: {e}")

if entity_col:
    top_df = pd.read_sql(f"SELECT {entity_col} AS entity, SUM(sales) AS total_sales FROM sales GROUP BY {entity_col} ORDER BY total_sales DESC LIMIT 10", engine)
else:
    top_df = pd.DataFrame()
    st.warning("No customer_name/customer_id/country/region column found in 'sales' table.")

# 3) RFM data
rfm_view = 'vw_rfm' if exists('vw_rfm') else ('vw_rfm_country' if exists('vw_rfm_country') else None)
rfm_df = pd.read_sql(f"SELECT * FROM {rfm_view} ORDER BY rfm_total DESC LIMIT 50", engine) if rfm_view else pd.DataFrame()

# 4) Cohort data
cohort_view = 'vw_cohort' if exists('vw_cohort') else ('vw_cohort_country' if exists('vw_cohort_country') else None)
cohort_df = pd.read_sql(f"SELECT * FROM {cohort_view} ORDER BY cohort_month DESC LIMIT 200", engine) if cohort_view else pd.DataFrame()

# --- Horizontal layout using columns ---
cols = st.columns(3)

# Top entities
with cols[0]:
    st.markdown("<div class='section-box'>", unsafe_allow_html=True)
    st.markdown(f"<h3 class='subheader-blue'>Top 10 by {entity_col.replace('_',' ').title() if entity_col else 'Entity'}</h3>", unsafe_allow_html=True)
    st.dataframe(top_df)
    st.markdown("</div>", unsafe_allow_html=True)

# RFM
with cols[1]:
    if not rfm_df.empty:
        st.markdown("<div class='section-box'>", unsafe_allow_html=True)
        st.markdown("<h3 class='subheader-green'>RFM Segments</h3>", unsafe_allow_html=True)
        st.dataframe(rfm_df)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("RFM view not found.")

# Cohort
with cols[2]:
    if not cohort_df.empty:
        st.markdown("<div class='section-box'>", unsafe_allow_html=True)
        st.markdown("<h3 class='subheader-orange'>Cohort Sample</h3>", unsafe_allow_html=True)
        st.dataframe(cohort_df)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("Cohort view not found.")

# 5) Monthly sales trend (full width)
st.markdown("<h2 style='color: #FF6347;'>Monthly sales</h2>", unsafe_allow_html=True)
try:
    monthly = pd.read_sql("SELECT DATE_TRUNC('month', order_date) AS month, SUM(sales) AS total_sales FROM sales GROUP BY month ORDER BY month", engine)
    monthly['month'] = pd.to_datetime(monthly['month'])
    st.line_chart(data=monthly.set_index('month')['total_sales'])
except Exception as e:
    st.error(f"Error loading monthly trend: {e}")


