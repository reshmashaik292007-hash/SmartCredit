
import streamlit as st
from theme import apply_theme

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SmartCredit - Risk Assessment",
    page_icon="📊",
    layout="wide"
)

apply_theme()

# ============================================================
# GET RESULTS
# ============================================================

if "probability" not in st.session_state:
    st.warning("No credit risk assessment found.")
    st.info("Please return to the Home page and analyze a borrower.")
    st.stop()

probability = st.session_state["probability"]
credit_score = st.session_state["credit_score"]
rating = st.session_state["rating"]

# ============================================================
# RESULT CARD STYLING
# ============================================================

st.markdown("""
<style>
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

.result-card {
    background: #1B2230;
    border: 1px solid #35445B;
    border-radius: 14px;
    padding: 24px 16px;
    text-align: center;
    min-height: 145px;
}

.result-title {
    color: #A0AEC0;
    font-size: 15px;
    margin-bottom: 15px;
}

.result-value {
    color: #F1F5F9;
    font-size: 30px;
    font-weight: 700;
}

.borrower-card {
    background: #1B2230;
    border: 1px solid #35445B;
    border-radius: 12px;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

st.title("📊 Credit Risk Assessment")

st.caption(
    "AI-powered analysis of the borrower's credit risk"
)

st.divider()

# ============================================================
# RESULT CARDS
# ============================================================

decimal_precision = 2

probability_display = f"{probability:.{decimal_precision}%}"

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="result-card">
        <div class="result-title">⚠️ Probability of Default</div>
        <div class="result-value">{probability_display}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="result-card">
        <div class="result-title">💳 Credit Score</div>
        <div class="result-value">{credit_score} / 900</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="result-card">
        <div class="result-title">🏅 Credit Rating</div>
        <div class="result-value">{rating}</div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# RISK LEVEL
# ============================================================

st.write("")
st.subheader("Risk Assessment")

if probability >= 0.60:
    st.error("🔴 Risk Level: High Risk")

elif probability >= 0.30:
    st.warning("🟠 Risk Level: Moderate Risk")

else:
    st.success("🟢 Risk Level: Low Risk")

# ============================================================
# BORROWER SUMMARY
# ============================================================

st.divider()
st.subheader("👤 Borrower Summary")

currency_symbols = {
    "INR (₹)": "₹",
    "USD ($)": "$",
    "EUR (€)": "€",
    "GBP (£)": "£"
}

currency = st.session_state.get("currency", "INR (₹)")
symbol = currency_symbols.get(currency, "₹")

c1, c2, c3 = st.columns(3)

with c1:
    st.write(f"**Age:** {st.session_state['age']}")
    st.write(f"**Income:** {symbol}{st.session_state['income']:,.0f}")
    st.write(f"**Loan Amount:** {symbol}{st.session_state['loan_amount']:,.0f}")

with c2:
    st.write(f"**Loan Tenure:** {st.session_state['loan_tenure']} months")
    st.write(f"**Average DPD:** {st.session_state['avg_dpd']}")
    st.write(f"**Delinquency Ratio:** {st.session_state['delinquency_ratio']}%")

with c3:
    st.write(f"**Credit Utilization:** {st.session_state['credit_utilization']}%")
    st.write(f"**Open Loan Accounts:** {st.session_state['open_accounts']}")
    st.write(f"**Loan Type:** {st.session_state['loan_type']}")

# ============================================================
# RISK INTERPRETATION
# ============================================================

st.divider()
st.subheader("💡 Risk Interpretation")

if probability >= 0.60:
    st.write(
        "The borrower has a relatively high estimated probability "
        "of default. Additional credit assessment may be appropriate."
    )

elif probability >= 0.30:
    st.write(
        "The borrower falls within a moderate estimated risk range. "
        "Additional financial information may help with assessment."
    )

else:
    st.write(
        "The borrower has a relatively low estimated probability "
        "of default based on the provided information."
    )

# ============================================================
# NAVIGATION
# ============================================================

st.divider()

if st.button("← Back to Borrower Details"):
    st.switch_page("Home.py")

# ============================================================
# DISCLAIMER
# ============================================================

st.markdown("""
<div style="
    text-align:center;
    margin-top:40px;
    padding:15px;
    color:#A0AEC0;
    font-size:12px;
">
Disclaimer: This application provides an estimated credit-risk
assessment for educational purposes and should not be used as
the sole basis for lending decisions.
</div>
""", unsafe_allow_html=True)
