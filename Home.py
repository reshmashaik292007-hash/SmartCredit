import streamlit as st
from prediction_helper import predict
from theme import apply_theme

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SmartCredit – AI Credit Risk Analyzer",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# THEME INITIALIZATION
# ============================================================


apply_theme()

# ============================================================
# APP TITLE
# ============================================================

st.title("SmartCredit – AI Credit Risk Analyzer")

st.caption(
    "AI-powered borrower risk assessment and credit scoring system"
)

# ============================================================
# HOW TO USE
# ============================================================

with st.expander("ℹ️ How to use the app"):

    st.write("""
    - **Age**: Enter your age between 18-100. Younger borrowers might have different risk profiles.
    - **Income**: Enter your annual income in INR. Higher income can reduce the likelihood of default.
    - **Loan Amount**: The total loan amount you are applying for. Larger loans tend to carry more risk.
    - **Loan to Income Ratio**: This is automatically calculated based on your income and loan amount.
    - **Loan Tenure**: The duration (in months) for which the loan is being taken.
    - **Average DPD**: The average number of days past due for your previous loans.
    - **Delinquency Ratio**: The percentage of delinquent accounts in your credit history.
    - **Credit Utilization Ratio**: The percentage of your credit that you're currently utilizing.
    - **Number of Open Loan Accounts**: The total number of open credit accounts you have.
    - **Residence Type**: Choose if you own, rent, or mortgage your home.
    - **Loan Purpose**: The reason for taking the loan.
    - **Loan Type**: Whether the loan is secured or unsecured.
    """)

# ============================================================
# INPUT SECTIONS
# ============================================================

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# ============================================================
# ROW 1
# ============================================================

with row1[0]:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        step=1,
        value=28
    )

with row1[1]:

    income = st.number_input(
        "Income",
        min_value=0,
        value=1200000
    )

with row1[2]:

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0,
        value=2560000
    )

# ============================================================
# LOAN TO INCOME RATIO
# ============================================================

loan_to_income_ratio = (
    loan_amount / income
    if income > 0
    else 0
)

with row2[0]:

    st.markdown(
        '<div style="margin-bottom: 8px;">Loan to Income Ratio</div>',
        unsafe_allow_html=True
    )

    ratio_bg = "#1B2230"
    ratio_border = "#35445B"
    ratio_text = "#F1F5F9"

    st.markdown(
        f"""
        <div style="
            border: 1px solid {ratio_border};
            border-radius: 10px;
            padding: 10px 12px;
            background-color: {ratio_bg};
            height: 42px;
            box-sizing: border-box;
            display: flex;
            align-items: center;
        ">
            <span style="
                font-size: 14px;
                color: {ratio_text};
            ">
                {loan_to_income_ratio:.2f}
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )
with row2[1]:

    loan_tenure_months = st.number_input(
        "Loan Tenure (months)",
        min_value=0,
        step=1,
        value=36
    )

with row2[2]:

    avg_dpd_per_delinquency = st.number_input(
        "Avg DPD",
        min_value=0,
        value=20
    )

# ============================================================
# ROW 3
# ============================================================

with row3[0]:

    delinquency_ratio = st.number_input(
        "Delinquency Ratio",
        min_value=0,
        max_value=100,
        step=1,
        value=30
    )

with row3[1]:

    credit_utilization_ratio = st.number_input(
        "Credit Utilization Ratio",
        min_value=0,
        max_value=100,
        step=1,
        value=30
    )

with row3[2]:

    num_open_accounts = st.number_input(
        "Open Loan Accounts",
        min_value=1,
        max_value=4,
        step=1,
        value=2
    )

# ============================================================
# ROW 4
# ============================================================

with row4[0]:

    residence_type = st.selectbox(
        "Residence Type",
        ["Owned", "Rented", "Mortgage"]
    )

with row4[1]:

    loan_purpose = st.selectbox(
        "Loan Purpose",
        ["Education", "Home", "Auto", "Personal"]
    )

with row4[2]:

    loan_type = st.selectbox(
        "Loan Type",
        ["Unsecured", "Secured"]
    )

# ============================================================
# ANALYZE CREDIT RISK
# ============================================================

st.write("")

if st.button(
    "🔍 Analyze Credit Risk",
    use_container_width=False
):

    # ========================================================
    # EXISTING ML PREDICTION
    # ========================================================

    probability, credit_score, rating = predict(
        age,
        income,
        loan_amount,
        loan_tenure_months,
        avg_dpd_per_delinquency,
        delinquency_ratio,
        credit_utilization_ratio,
        num_open_accounts,
        residence_type,
        loan_purpose,
        loan_type
    )

    # ========================================================
    # STORE PREDICTION RESULTS
    # ========================================================

    st.session_state["probability"] = probability
    st.session_state["credit_score"] = credit_score
    st.session_state["rating"] = rating

    # ========================================================
    # STORE BORROWER INFORMATION
    # ========================================================

    st.session_state["age"] = age
    st.session_state["income"] = income
    st.session_state["loan_amount"] = loan_amount
    st.session_state["loan_tenure"] = loan_tenure_months
    st.session_state["avg_dpd"] = avg_dpd_per_delinquency
    st.session_state["delinquency_ratio"] = delinquency_ratio
    st.session_state["credit_utilization"] = credit_utilization_ratio
    st.session_state["open_accounts"] = num_open_accounts
    st.session_state["residence"] = residence_type
    st.session_state["purpose"] = loan_purpose
    st.session_state["loan_type"] = loan_type

    # ========================================================
    # GO TO RESULTS PAGE
    # ========================================================

    st.switch_page("pages/2_Results.py")