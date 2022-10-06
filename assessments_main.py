"""importing libraries"""
import streamlit as st
import pandas as pd
from PIL import Image

# INITIAL PAGE LAYOUT SETTINGS
favicon_img = Image.open("images/ziphire_favicon.ico")
st.set_page_config(
        page_title = "Ziphire HR",
        initial_sidebar_state = "auto",
        page_icon = favicon_img,
        layout = "centered"
)


def break_loop():
    """creating space"""
    i = 0
    while i < 4:
        st.markdown('<p></p>', unsafe_allow_html = True)
        i += 1

main_img = Image.open("images/ziphire_logo.png")

st.image(main_img, width = 150, output_format = 'PNG')

# data transformation
main_dataframe = pd.read_csv('data/ziphire_assessments.csv')

industry_list = main_dataframe['Tech Industry'].unique().tolist()
industry = st.selectbox('Choose Tech Industry :', industry_list)
chosen_industry_df = main_dataframe[main_dataframe['Tech Industry'] == industry]
break_loop()

skill_list = chosen_industry_df['Skill'].unique().tolist()
skill = st.selectbox('Choose SKill :', skill_list)
chosen_skill_df = chosen_industry_df[chosen_industry_df['Skill'] == skill]
break_loop()

juniorTEST = chosen_skill_df['Junior'].tolist()
mid_levelTEST = chosen_skill_df['Mid-Level'].tolist()
seniorTEST = chosen_skill_df['Senior'].tolist()

values = st.select_slider('Difficulty Level', ['Junior', 'Mid-Level', 'Senior'])

if values == 'Junior':

    st.header(' '.join(juniorTEST))

elif values == 'Mid-Level':

    st.header(' '.join(mid_levelTEST))

elif values == 'Senior':

    st.header(' '.join(seniorTEST))
