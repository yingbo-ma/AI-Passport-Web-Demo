# page_2

import streamlit as st
from langchain.llms import OpenAI

def app():
    st.title('Notebook Exercise')

    openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
    def generate_response(input_text):
        llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
        st.info(llm(input_text))


    # section 1: getting started with llms
    st.header('Getting Started with LLMs', divider='rainbow')

    # assignment 1: summarizing
    st.write('Assignment 1: Automatically generating discharge summaries for a patient with Type 2 diabetes.')

    with st.form('my_form_1'):
        text = st.text_area('To get started, please enter your OpenAI API key in the side bar.', label_visibility='collapsed')
        submitted = st.form_submit_button('Submit')
        if submitted and openai_api_key.startswith('sk-'):
            generate_response(text) 
    

    # assignment 2: prior authorization medication
    st.write('Assignment 2: Prior authorized medication.')

    with st.form('my_form_2'):
        text = st.text_area('Prior authorized medication.', 'To get started, please enter your OpenAI API key in the side bar.', label_visibility='collapsed')
        submitted = st.form_submit_button('Submit')
        if submitted and openai_api_key.startswith('sk-'):
            generate_response(text) 

    # assignment 3: llm for a customized use case
    st.write('Assignment 3: Summarize the latest guidelines for managing Type 2 diabetes.')

    with st.form('my_form_3'):
        text = st.text_area('LLM for a special use', 'To get started, please enter your OpenAI API key in the side bar.', label_visibility='collapsed')
        submitted = st.form_submit_button('Submit')
        if submitted and openai_api_key.startswith('sk-'):
            generate_response(text) 

    st.header('Assignment 2', divider='rainbow')

    st.header('Assignment 3', divider='rainbow')

    st.header('Assignment 4', divider='rainbow')