import streamlit as st

from PIL import Image
image_learn_more_about_us = Image.open('images/learn_more_about_us.png')

def app():
    st.image(image_learn_more_about_us)