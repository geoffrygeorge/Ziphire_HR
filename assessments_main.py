"""importing libraries"""
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
from platforms import xobin

# INITIAL PAGE LAYOUT SETTINGS
favicon_img = Image.open("images/ziphire_favicon.ico")
st.set_page_config(
        page_title = "Ziphire HR",
        initial_sidebar_state = "auto",
        page_icon = favicon_img,
        layout = "centered"
)


st.markdown("""
    <style>
    .css-15zrgzn {display: none}
    .css-eczf16 {display: none}
    .css-cveqeb {display: none}
    </style>
    """, unsafe_allow_html=True)

main_img = Image.open("images/ziphire_logo.png")

st.sidebar.image(main_img, width = 150, output_format = 'PNG')

st.sidebar.title("NAVIGATION")

# defining various pages in the application
main_menu = ['HOME', 'XOBIN', 'HACKEREARTH']

with st.container():

    menu = st.sidebar.selectbox('Go to', main_menu)

if menu == 'XOBIN':

    xobin.xobin_main()
    