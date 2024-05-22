# page_1.py

import streamlit as st

def app():
    st.title('Instructional Videos')

    st.header('Video 1: Introduction to Generative AI and LLMs')
    video_url = "https://www.youtube.com/watch?v=G2fqAlgmoPo"
    st.video(video_url)

    st.header('Video 2: LLMs for Health')
    video_url = "https://www.youtube.com/watch?v=k_-Z_TkHMqA"
    st.video(video_url)