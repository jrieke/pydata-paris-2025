import streamlit as st

st.set_page_config(page_title="PyData Paris 2025", page_icon="🇫🇷")
st.logo(
    "https://streamlit.io/images/brand/streamlit-mark-color.svg",
    link="https://streamlit.io",
)

page = st.navigation(
    [
        st.Page("home.py", title="Home", icon="🏠"),
        st.Page("dashboard.py", title="Dashboard", icon="📊"),
    ],
    position="top",
)
page.run()
