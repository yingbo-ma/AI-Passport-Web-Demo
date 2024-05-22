import streamlit as st

from PIL import Image
image = Image.open('images/learning_experience.png')

def app():
    st.title("See-Practice-Share-Reflect (SPACER) Framework")
    st.write("Our innovative training approach, grounded in Kolb’s experiential learning theory (Figure below), fosters holistic and experiential learning embedded within a digital community of practice. While for the SPACER approach learning the technical content is a must, equal amounts of time are dedicated to actively engaging with the content, applying it, discussing it with peers, and critically reflecting upon its relevance to one's own research or career. Each module will use a toolkit of activities developed within this framework.")
    
    st.image(image=image)