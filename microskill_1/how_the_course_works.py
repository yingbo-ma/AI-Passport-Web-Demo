import streamlit as st
from PIL import Image

image = Image.open('images/module_breakdown.png')

def app():
    st.title('In This Module')
    st.write('Participants will receive a comprehensive, practical introduction to the essential principles of large language models (LLMs). Users will gain skills in utilizing, developing, and validating LLMs, as well as addressing issues related to human alignment and the risk of generating inaccurate information. The course will cover techniques for adjusting input prompts to obtain specific results (prompt engineering) and will explore the use of LLMs in clinical environments. Users will practice using LLMs for scientific data analysis and visualization with advanced code-generation tools.')

    st.image(image, caption='Module breakdown')