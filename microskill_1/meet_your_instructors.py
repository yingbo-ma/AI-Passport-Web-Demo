import streamlit as st

from PIL import Image
image_instructors = Image.open('images/instructors.png')

def app():
    st.image(image_instructors)