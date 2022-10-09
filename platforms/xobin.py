"""importing libraries"""
import streamlit as st
import pandas as pd

def xobin_main():
    """xobin assessment selector"""

    def break_loop():
        """creating space"""
        i = 0
        while i < 3:
            st.markdown('<p></p>', unsafe_allow_html = True)
            i += 1

    st.markdown("""
        <style>
        .big-font {
            text-align: center;
            padding-top: 0.5px;
            font-size: calc(0.50em + 4.0vmin);
            font-family: sans-serif;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html = True)

    st.markdown('<p class="big-font">XOBIN ASSESSMENT SELECTOR</p>', unsafe_allow_html = True)

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
    juniorTEST_md = ' '.join(juniorTEST)
    mid_levelTEST = chosen_skill_df['Mid-Level'].tolist()
    mid_levelTEST_md = ' '.join(mid_levelTEST)
    seniorTEST = chosen_skill_df['Senior'].tolist()
    seniorTEST_md = ' '.join(seniorTEST)

    values = st.radio('Difficulty Level :', ['Junior', 'Mid-Level', 'Senior'], horizontal = True)

    if values == 'Junior':

        st.markdown("""
        <style>
        .small-font {
            text-align: center;
            text-decoration: none;
            padding-top: 0.5px;
            font-size: calc(0.50em + 2.0vmin);
            font-family: sans-serif;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html = True)

        break_loop() # <a href="https://streamlit.io/">{temp}</a>

        st.markdown('<p class="small-font">{temp}</p>'.format(temp = juniorTEST_md), unsafe_allow_html = True)

    elif values == 'Mid-Level':

        st.markdown("""
        <style>
        .small-font {
            text-align: center;
            padding-top: 0.5px;
            font-size: calc(0.50em + 2.0vmin);
            font-family: sans-serif;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html = True)

        break_loop()

        st.markdown('<p class="small-font">{temp}</p>'.format(temp = mid_levelTEST_md), unsafe_allow_html = True)

    elif values == 'Senior':

        st.markdown("""
        <style>
        .small-font {
            text-align: center;
            padding-top: 0.5px;
            font-size: calc(0.50em + 2.0vmin);
            font-family: sans-serif;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html = True)

        break_loop()

        st.markdown('<p class="small-font">{temp}</p>'.format(temp = seniorTEST_md), unsafe_allow_html = True)
