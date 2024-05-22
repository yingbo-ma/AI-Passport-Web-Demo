import streamlit as st

from PIL import Image
image_welcome = Image.open('images/background.png')
welcome_whats_included = Image.open('images/whats_included.png')

def app():
    st.title('Welcome to AI Passport!')
    st.write('AI Passport for Health is an open, scalable training program designed as a digital learning community for healthcare professionals. Participants engage with AI faculty, coaches, and mentors to acquire skills for integrating AI into their research. AIPassport stands out for its agility and minimal coding requirements, making it accessible to learners of all technical levels. The program emphasizes practical learning through medical case studies, combining asynchronous learning with live community-based sessions and peer mentoring, offering a unique virtual learning experience with real-world data exercises.')    
    st.write('Questions? Issues? Reach out to xxx@ufl.edu for help!')
    st.image(image_welcome)

    st.header("What's Included")
    st.image(welcome_whats_included)