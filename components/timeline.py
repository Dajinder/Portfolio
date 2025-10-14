import streamlit as st
from streamlit_timeline import timeline

def get_timeline_data():
    """Return timeline data"""
    return {
        "title": {
            "text": {
                "headline": "My Professional Journey",
                "text": "Education and Work Experience Timeline"
            }
        },
        "events": [
            {
                "start_date": {
                    "year": "2017",
                    "month": "08",
                    "day": "01"
                },
                "end_date": {
                    "year": "2021",
                    "month": "06",
                    "day": "30"
                },
                "text": {
                    "headline": "B.Tech (IT), GGSIPU",
                    "text": "Completed Bachelors of Technology in Information Technology from GGSIPU with GPA of 8 out of 10."
                },
                "group": "Education",
                "background": {
                    "color": "#2196F3"
                }
            },
            {
                "start_date": {
                    "year": "2020",
                    "month": "12",
                    "day": "01"
                },
                "end_date": {
                    "year": "2021",
                    "month": "05",
                    "day": "31"
                },
                "text": {
                    "headline": "Business Analyst Intern, ZS",
                    "text": "Created and managed reports using Qlik Sense for Sales and Field Force data of Pharma Clients. Delivered weekly development and operational reports to clients. Performed quality analysis of data with SQL and Excel."
                },
                "group": "Work"
            },
            {
                "start_date": {
                    "year": "2021",
                    "month": "06",
                    "day": "01"
                },
                "end_date": {
                    "year": "2022",
                    "month": "12",
                    "day": "31"
                },
                "text": {
                    "headline": "Business Technology Associate, ZS",
                    "text": "Performed Development, Testing and Deployment of reports on Qlik Sense and Salesforce. Facilitated transition of reports from Qlik Sense to Salesforce CRM Platform. Conducted data quality analysis and documentation such as Requirement Gathering, BRD, FRS etc."
                },
                "group": "Work",
                "background": {
                    "color": "#4CAF50"
                }
            },
            {
                "start_date": {
                    "year": "2023",
                    "month": "01",
                    "day": "01"
                },
                "end_date": {
                    "year": "2023",
                    "month": "11",
                    "day": "30"
                },
                "text": {
                    "headline": "Senior Data Engineer, ZS",
                    "text": "Designed and optimized data pipelines for Incentive Compensation data for Sales using Informatica (IICS) and Snowflake. Automated triggers with Autosys and shell scripts. Reduced process runtime from 8 hours to 2.5 hours, enhancing overall efficiency. Managed deployment of data pipelines, tables and other dependencies between environments using Windchill tool."
                },
                "group": "Work",
                "background": {
                    "color": "#4CAF50"
                }
            },
            {
                "start_date": {
                    "year": "2023",
                    "month": "12",
                    "day": "01"
                },
                "end_date": {
                    "year": "2025",
                    "month": "01",
                    "day": "31"
                },
                "text": {
                    "headline": "Business Technology Associate Consultant, ZS",
                    "text": "Led business analysis for requirement gathering, documentation, testing, and project delivery for Pricing project of major pharmaceutical clients. Authored User Requirement Specifications (URS), Functional Requirement Specifications (FRS), and User Acceptance Testing (UAT) documentation. Implemented Agile methodology using JIRA, resulting in a 40% increase in project efficiency. Promoted to Business Technology Associate Consultant Role."
                },
                "group": "Work",
                "background": {
                    "color": "#4CAF50"
                }
            },
            {
                "start_date": {
                    "year": "2025",
                    "month": "01",
                    "day": "01"
                },
                "end_date": {
                    "year": "2026",
                    "month": "06",
                    "day": "01"
                },
                "text": {
                    "headline": "Masters in Applied Computing, University of Windsor",
                    "text": "Pursuing Master of Applied Computing to upskill in AI and ML."
                },
                "group": "Education",
                "background": {
                    "color": "#2196F3"
                }
            }
        ]
    }

def render():
    """Render the timeline section"""
    with st.container():
        st.markdown('<div id="experience" class="py-8">', unsafe_allow_html=True)
        st.title("Career Timeline")
        
        # Render the timeline with increased height for better visibility
        timeline(get_timeline_data(), height=800)
        
        st.markdown('</div><hr>', unsafe_allow_html=True)
