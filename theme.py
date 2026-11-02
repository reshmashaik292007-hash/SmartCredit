
import streamlit as st


def apply_theme():

    background = "#0E1117"
    sidebar = "#151B26"
    surface = "#1B2230"
    surface_2 = "#252F40"
    border = "#35445B"
    text = "#F1F5F9"
    secondary = "#A0AEC0"
    accent = "#3B82F6"

    st.markdown(
        f"""
        <style>

        /* Main application */
        .stApp {{
            background-color: {background} !important;
            color: {text} !important;
        }}

        .main .block-container {{
            background-color: {background} !important;
            color: {text} !important;
            padding-top: 2rem;
        }}

        /* Header and toolbar */
        header[data-testid="stHeader"] {{
            background-color: {background} !important;
        }}

        [data-testid="stToolbar"] {{
            background-color: {background} !important;
        }}

        /* Sidebar */
        section[data-testid="stSidebar"] {{
            background-color: {sidebar} !important;
        }}

        section[data-testid="stSidebar"] * {{
            color: {text} !important;
        }}

        [data-testid="stSidebarNav"] a {{
            border-radius: 8px;
        }}

        [data-testid="stSidebarNav"] a:hover,
        [data-testid="stSidebarNav"] a[aria-current="page"] {{
            background-color: {surface_2} !important;
        }}

        /* Text */
        h1, h2, h3, h4, h5, h6,
        p, label, span, li {{
            color: {text};
        }}

        [data-testid="stCaptionContainer"] p {{
            color: {secondary} !important;
        }}

        /* Number and text inputs */
        div[data-testid="stNumberInput"] > div,
        div[data-testid="stTextInput"] > div,
        div[data-testid="stTextArea"] > div,
        div[data-testid="stDateInput"] > div {{
            background-color: {surface} !important;
            border: 1px solid {border} !important;
            border-radius: 9px !important;
        }}

        input, textarea {{
            background-color: {surface} !important;
            color: {text} !important;
            -webkit-text-fill-color: {text} !important;
        }}

        /* Select boxes */
        div[data-baseweb="select"] > div {{
            background-color: {surface} !important;
            border-color: {border} !important;
            color: {text} !important;
        }}

        div[data-baseweb="select"] span {{
            color: {text} !important;
        }}

        /* Dropdown menus */
        div[data-baseweb="popover"],
        div[data-baseweb="menu"],
        ul[data-baseweb="menu"] {{
            background-color: {surface} !important;
            color: {text} !important;
        }}

        /* Buttons */
        .stButton > button {{
            background-color: {accent} !important;
            color: white !important;
            border: none !important;
            border-radius: 9px !important;
            font-weight: 600 !important;
        }}

        .stButton > button p {{
            color: white !important;
        }}

        .stButton > button:hover {{
            background-color: #2563EB !important;
        }}

        /* Cards and metrics */
        [data-testid="stMetric"],
        [data-testid="stExpander"],
        [data-testid="stAlert"] {{
            background-color: {surface} !important;
            border: 1px solid {border} !important;
            border-radius: 10px !important;
        }}

        [data-testid="stMetricLabel"],
        [data-testid="stMetricValue"] {{
            color: {text} !important;
        }}

        /* Tabs */
        button[data-baseweb="tab"] {{
            color: {text} !important;
        }}

        /* Dataframes */
        [data-testid="stDataFrame"],
        [data-testid="stTable"] {{
            background-color: {surface} !important;
        }}

        /* Dividers */
        hr {{
            border-color: {border} !important;
        }}

        /* Links */
        a {{
            color: #60A5FA !important;
        }}

        /* Mobile */
        @media (max-width: 768px) {{
            .block-container {{
                padding-left: 1rem;
                padding-right: 1rem;
            }}
        }}

        </style>
        """,
        unsafe_allow_html=True
    )
