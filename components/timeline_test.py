import streamlit as st
from streamlit_timeline import timeline

def get_timeline_data():
    return {
        "title": {
            "text": {
                "headline": "My Journey",
                "text": "Education and Professional Experience"
            }
        },
        "events": [
            {
                "start_date": {
                    "year": "2017",
                    "month": "08"
                },
                "end_date": {
                    "year": "2021",
                    "month": "06"
                },
                "text": {
                    "headline": "B.Tech (IT), GGSIPU",
                    "text": "Completed Bachelors of Technology in Information Technology from GGSIPU"
                }
            }
        ]
    }

def render():
    st.title("Timeline Test")
    timeline(get_timeline_data())