"""importing libraries"""
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import requests
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

if menu == 'HOME':

    st.markdown("""
        <style>
        .big-font {
            text-align: center;
            padding-top: 0.5px;
            font-size: calc(0.50em + 4.0vmin);
            font-family: 'Trebuchet MS', sans-serif;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html = True)

    st.markdown('<p class="big-font">ZIPHIRE ASSESSMENT SELECTOR</p>', unsafe_allow_html = True)

    st.markdown('<p></p>', unsafe_allow_html = True)

    LOTTIE_URL = "https://assets4.lottiefiles.com/packages/lf20_ij2ngolf.json"
    @st.cache(show_spinner = False)
    def intro_lottie(url: str):
        """defining function for lottie"""
        r = requests.get(url)
        if r.status_code != 200:
            return None

        return r.json()

    lottie_returned = intro_lottie(LOTTIE_URL)

    st_lottie(lottie_returned, height = 500, quality = "high", speed = 1.5)


if menu == 'XOBIN':

    xobin.xobin_main()

if menu == 'HACKEREARTH':

    st.markdown("""
        <style>
        .big-font {
            text-align: center;
            padding-top: 0.5px;
            font-size: calc(0.50em + 4.0vmin);
            font-family: 'Trebuchet MS', sans-serif;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html = True)

    st.markdown('<p class="big-font">UNDER CONSTRUCTION</p>', unsafe_allow_html = True)
    