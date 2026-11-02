
import streamlit as st
from theme import apply_theme

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="About - SmartCredit",
    page_icon="ℹ️",
    layout="wide"
)

apply_theme()

# ============================================================
# HEADER
# ============================================================

st.title("ℹ️ About SmartCredit")

st.caption(
    "AI-powered credit risk assessment and borrower analysis"
)

st.divider()

# ============================================================
# PROJECT OVERVIEW
# ============================================================

st.subheader("About the Project")

st.write("""
SmartCredit is an AI-powered Credit Risk Prediction application
designed to estimate a borrower's creditworthiness using
machine learning.

The application analyzes borrower information and financial
indicators to generate an estimated probability of default,
credit score, and credit rating.
""")

# ============================================================
# UNDERSTANDING CREDIT RISK
# ============================================================

st.subheader("Understanding Credit Risk")

with st.expander("⚠️ Probability of Default"):
    st.write("""
    Probability of Default represents the estimated likelihood
    that a borrower may fail to repay a loan.

    A higher percentage indicates a higher estimated risk.
    """)

with st.expander("💳 Credit Score"):
    st.write("""
    Credit score is a numerical representation of estimated
    creditworthiness.

    In SmartCredit, the score ranges from 300 to 900.
    Higher scores generally indicate better creditworthiness.
    """)

with st.expander("🏅 Credit Rating"):
    st.write("""
    Credit rating classifies the borrower's estimated
    creditworthiness into categories such as Poor, Average,
    Good, or Excellent.
    """)

with st.expander("🚦 Risk Level"):
    st.write("""
    Risk level summarizes the estimated probability of default
    into three categories:

    - Low Risk
    - Moderate Risk
    - High Risk
    """)

# ============================================================
# PROJECT FEATURES
# ============================================================

st.divider()

st.subheader("Key Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🤖")
    st.markdown("**ML Prediction**")
    st.caption("Machine learning-based credit risk estimation.")

with col2:
    st.markdown("### 📊")
    st.markdown("**Credit Analysis**")
    st.caption("Credit score and probability of default.")

with col3:
    st.markdown("### 💡")
    st.markdown("**Risk Insights**")
    st.caption("Understand borrower risk through clear results.")

# ============================================================
# DISCLAIMER
# ============================================================

st.divider()

st.info("""
**Disclaimer:** SmartCredit is an educational project.
Its predictions are estimates and should not be used as
the sole basis for actual lending decisions.
""")

st.caption("SmartCredit | AI Credit Risk Analyzer")
