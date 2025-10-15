import streamlit as st
from streamlit_timeline import timeline
import json
from datetime import datetime

def get_time_period(start_date, end_date):
    """Calculate the time period between two dates"""
    start = datetime.strptime(f"{start_date['year']}-{start_date['month']}-{start_date['day']}", "%Y-%m-%d")
    end = datetime.strptime(f"{end_date['year']}-{end_date['month']}-{end_date['day']}", "%Y-%m-%d")
    diff = end - start
    years = diff.days / 365.25
    if years >= 1:
        return f"{years:.1f} years"
    else:
        months = diff.days / 30.44
        return f"{months:.0f} months"

def get_timeline_data():
    """Return timeline data with professional color gradients"""
    # Professional color gradients
    education_gradient = {
        "color": "#2196F3",
        "gradient": "linear-gradient(135deg, #2196F3 0%, #21CBF3 100%)"
    }
    work_gradient = {
        "color": "#4CAF50",
        "gradient": "linear-gradient(135deg, #4CAF50 0%, #45B649 100%)"
    }
    
    return {
        "title": {
            "text": {
                "headline": "My Professional Journey",
                "text": "Education and Work Experience Timeline"
            },
            "background": {
                "gradient": "linear-gradient(135deg, #1a237e 0%, #0d47a1 100%)",
                "opacity": 0.8,
                "color": "#1a237e"
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
                "background": education_gradient
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
                    "headline": "Business Analyst Intern, ZS Associates",
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
                    "headline": "Business Technology Solutions Assocciate, ZS Associates",
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
                    "headline": "Business Technology Solutions Associate, ZS Associates",
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
                    "day": "02"
                },
                "text": {
                    "headline": "Business Technology Solutions Associate Consultant, ZS Associates",
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
                    "day": "14"
                },
                "end_date": {
                    "year": "2026",
                    "month": "04",
                    "day": "30"
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
        st.markdown('<div id="experience" class="timeline-component">', unsafe_allow_html=True)
        
        # Header section with interactive filters
        col1, col2 = st.columns([2, 1])
        with col1:
            st.title("Career Timeline")
            st.markdown("*Click on events to see detailed information*")
        with col2:
            view_filter = st.selectbox("Filter by", ["All", "Education", "Work"], key="timeline_filter")
        
        # Get timeline data
        timeline_data = get_timeline_data()
        
        # Apply filters
        if view_filter != "All":
            filtered_events = [
                event for event in timeline_data["events"]
                if event["group"] == view_filter
            ]
            timeline_data["events"] = filtered_events
        
        # Calculate dynamic height based on number of events
        timeline_height = min(max(400, len(timeline_data["events"]) * 100), 800)
        
        # Render timeline
        try:
            selected = timeline(
                timeline_data,
                height=timeline_height
            )
            
            # Show details of selected event with enhanced styling
            if selected is not None and isinstance(selected, dict):
                with st.expander("📋 Event Details", expanded=True):
                    selected_headline = selected.get("text", {}).get("headline")
                    if selected_headline:
                        event = next((e for e in timeline_data["events"] 
                                    if e["text"]["headline"] == selected_headline), None)
                        if event:
                            duration = get_time_period(event["start_date"], event["end_date"])
                            
                            # Professional gradients based on group
                            gradient = "linear-gradient(135deg, #2196F3 0%, #21CBF3 100%)" if event["group"] == "Education" else "linear-gradient(135deg, #4CAF50 0%, #45B649 100%)"
                            text_color = "#1a237e" if event["group"] == "Education" else "#1b5e20"
                            
                            st.markdown(f"""
                            <div style="
                                padding: 25px;
                                border-radius: 10px;
                                background: {gradient};
                                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                                color: white;
                                transition: all 0.3s ease;
                                margin: 10px 0;
                            ">
                                <h3 style="
                                    color: white;
                                    font-weight: 600;
                                    margin-bottom: 15px;
                                ">{event["text"]["headline"]}</h3>
                                <div style="
                                    background: rgba(255,255,255,0.95);
                                    padding: 15px;
                                    border-radius: 8px;
                                    color: {text_color};
                                ">
                                    <p style="font-size: 1.1em; margin-bottom: 10px;">
                                        <strong>⏱ Duration:</strong> {duration}
                                    </p>
                                    <p style="font-size: 1.1em; margin-bottom: 10px;">
                                        <strong>🎯 Type:</strong> {event["group"]}
                                    </p>
                                    <p style="
                                        line-height: 1.6;
                                        margin-top: 15px;
                                        color: #333;
                                    ">{event["text"]["text"]}</p>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Error displaying timeline: {str(e)}")
            st.markdown("Please try refreshing the page")
