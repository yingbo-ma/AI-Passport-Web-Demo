import streamlit as st

from PIL import Image
image_what_makes_us_unique = Image.open('images/what_makes_us_unique.png')
image_strategic_plan = Image.open('images/strategic_initiative_plan.png')

images_on_page = [image_what_makes_us_unique,image_strategic_plan]

def app():
    st.image(images_on_page)