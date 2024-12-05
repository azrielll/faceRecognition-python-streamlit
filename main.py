import streamlit as st

st.set_page_config(page_title="Absensi")

# Home Page
home_page = st.Page(
    page = "pages/home.py",
    title = "Home",
    icon = "🏠",
    default=True
)

# Login Page
login_page = st.Page(
    page = "pages/login.py",
    title = "Login",
    icon = "📷",
)
# Register Page
register_page = st.Page(
    page = "pages/register.py",
    title = "Register",
    icon = "®️",
)

# Data Page
data_page = st.Page(
    page = "pages/database.py",
    title = "Database",
    icon = "📅",
)

# Navigation
pg = st.navigation([home_page,login_page, register_page,data_page])


pg.run()