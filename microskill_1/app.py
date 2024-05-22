"""

AI Passport website demo codes
Author: Yingbo Ma
Date: May 21, 2024

"""

# Main Entry Point
import streamlit as st

import welcome
import how_the_course_works
import learning_experience

import microskill_1_intro
import microskill_2_intro
import microskill_3_intro
import microskill_4_intro
import what_makes_us_unique
import meet_your_instructors
import learn_more

from microskill_1 import page_1
from microskill_1 import page_2
from microskill_1 import page_3
from microskill_1 import page_4

PAGES = {
    "Welcome to AI Passport!": welcome,
    "How This Course Works": how_the_course_works,
    "Learning Experience": learning_experience,
    "Microskill 1": microskill_1_intro,
    "Microskill 2": microskill_2_intro,
    "Microskill 3": microskill_3_intro,
    "Microskill 4": microskill_4_intro,
    "What Makes Us Unique": what_makes_us_unique,
    "Meet Your Instructors": meet_your_instructors,
    "Learn More About Us": learn_more,
    "See - Watch the Video": page_1,
    "Practice - Work on Notebook Exercise": page_2,
    "Share - Interact with AI Coaches and Mentors": page_3,
    "Reflect - Tie the Learning to Practical Scenarios": page_4
}

main_page_names = ["Welcome to AI Passport!", 
                   "How This Course Works",
                   "Learning Experience",
                   "Microskill 1",
                   "Microskill 2",
                   "Microskill 3",
                   "Microskill 4",
                   "What Makes Us Unique",
                   "Meet Your Instructors",
                   "Learn More About Us"
                   ]

module_1_sub_page_names = ["Microskill 1",
                  "See - Watch the Video", 
                  "Practice - Work on Notebook Exercise",
                  "Share - Interact with AI Coaches and Mentors", 
                  "Reflect - Tie the Learning to Practical Scenarios"
                  ]

# Initialize session state variables if not already initialized
for page_name in PAGES.keys():
    if f'visited_{page_name}' not in st.session_state:
        st.session_state[f'visited_{page_name}'] = False

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", main_page_names)

if selection == "Microskill 1":
    st.sidebar.markdown("---")
    sub_selection = st.sidebar.radio("Sub-tasks under Microskill 1", module_1_sub_page_names)
    selection = sub_selection  # Change selection to sub-selection

if selection == "Microskill 2":
    st.sidebar.markdown("---")
    sub_selection = st.sidebar.radio("Sub-tasks under Microskill 2", sub_page_names)
    selection = sub_selection  # Change selection to sub-selection

if selection == "Microskill 3":
    st.sidebar.markdown("---")
    sub_selection = st.sidebar.radio("Sub-tasks under Microskill 3", sub_page_names)
    selection = sub_selection  # Change selection to sub-selection

if selection == "Microskill 4":
    st.sidebar.markdown("---")
    sub_selection = st.sidebar.radio("Sub-tasks under Microskill 4", sub_page_names)
    selection = sub_selection  # Change selection to sub-selection

page = PAGES[selection]
page.app()

# Update session state after selection
st.session_state[f'visited_{selection}'] = True