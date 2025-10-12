import streamlit as st
from streamlit_timeline import st_timeline

def get_timeline_data():
    """Return timeline data"""
    return [
        {
            "id": 1, 
            "content": "B.Tech (IT), GGSIPU", 
            "start": "2017-08-01", 
            "end": "2021-06-30", 
            "group": "Education",
            "title": "Completed Bachelors of Technology in Information Technology from GGSIPU with GPA of 8 out of 10."
        },
        {
            "id": 2, 
            "content": "Business Analyst Intern, ZS", 
            "start": "2020-12-01", 
            "end": "2021-05-31", 
            "group": "Work",
            "title": "Created and managed reports using Qlik Sense for Sales and Field Force data of Pharma Clients. Delivered weekly development and operational reports to clients. Performed quality analysis of data with SQL and Excel."
        },
        {
            "id": 3, 
            "content": "Business Technology Associate, ZS", 
            "start": "2021-06-01", 
            "end": "2022-12-31",  
            "group": "Work",
            "title": "Performed Development, Testing and Deployment of reports on Qlik Sense and Salesforce. Facilitated transition of reports from Qlik Sense to Salesforce CRM Platform. Conducted data quality analysis and documentation such as Requirement Gathering, BRD, FRS etc."
        },
        {
            "id": 4, 
            "content": "Senior Data Engineer, ZS", 
            "start": "2023-01-01",  
            "end": "2023-11-30", 
            "group": "Work",
            "title": "Designed and optimized data pipelines for Incentive Compensation data for Sales using Informatica (IICS) and Snowflake. Automated triggers with Autosys and shell scripts. Reduced process runtime from 8 hours to 2.5 hours, enhancing overall efficiency. Managed deployment of data pipelines, tables and other dependencies between environments using Windchill tool."
        },
        {
            "id": 5, 
            "content": "Business Technology Associate Consultant, ZS", 
            "start": "2023-12-01", 
            "end": "2025-01-31",  
            "group": "Work",
            "title": "Led business analysis for requirement gathering, documentation, testing, and project delivery for Pricing project of major pharmaceutical clients. Authored User Requirement Specifications (URS), Functional Requirement Specifications (FRS), and User Acceptance Testing (UAT) documentation. Implemented Agile methodology using JIRA, resulting in a 40% increase in project efficiency. Promoted to Business Technology Associate Consultant Role."
        },
        {
            "id": 6, 
            "content": "Masters in Applied Computing, University of Windsor", 
            "start": "2025-01-01", 
            "end": "2026-06-01", 
            "group": "Education",
            "title": "Pursuing Master of Applied Computing to upskill in AI and ML."
        }
    ]

@st.dialog("📋 Details")
def show_timeline_dialog(event):
    """Show timeline event details in dialog"""
    if event:
        icon = "🎓" if event["group"] == "Education" else "💼"
        st.markdown(f"### {icon} {event['content']}")
        st.write(event["title"])
        st.write(f"**Start:** {event['start']}")
        if "end" in event and event["end"]:
            st.write(f"**End:** {event['end']}")

def render():
    """Render the timeline section"""
    
    # Initialize timeline-specific session state
    if "last_timeline_click" not in st.session_state:
        st.session_state.last_timeline_click = None
    if "timeline_trigger_dialog" not in st.session_state:
        st.session_state.timeline_trigger_dialog = False
    if "timeline_selected_event_data" not in st.session_state:
        st.session_state.timeline_selected_event_data = None
    
    timeline_data = get_timeline_data()
    education_items = [i for i in timeline_data if i["group"] == "Education"]
    work_items = [i for i in timeline_data if i["group"] == "Work"]
    
    with st.container():
        st.markdown('<div id="experience" class="py-8">', unsafe_allow_html=True)
        st.title("Career Timeline")
        
        # Education timeline
        st.subheader("🎓 Education Timeline")
        selected_edu = st_timeline(
            items=education_items,
            groups=[],
            options={"clickToUse": True, "selectable": True},
            height="200px",
            key="edu_timeline_widget"
        )
        
        # Work timeline
        st.subheader("💼 Professional Timeline: ZS Associates PVT LTD.")
        selected_work = st_timeline(
            items=work_items,
            groups=[],
            options={"clickToUse": True, "selectable": True},
            height="300px",
            key="work_timeline_widget"
        )
        
        # Handle selections - only process if from timeline widgets
        selected_event = None
        event_id = None
        
        # Check education selection
        if selected_edu:
            if isinstance(selected_edu, dict) and "id" in selected_edu:
                event_id = selected_edu["id"]
            elif isinstance(selected_edu, list) and len(selected_edu) > 0:
                event_id = selected_edu[0]
            
            if event_id and event_id != st.session_state.last_timeline_click:
                selected_event = next((e for e in education_items if e["id"] == event_id), None)
                if selected_event:
                    st.session_state.last_timeline_click = event_id
                    st.session_state.timeline_selected_event_data = selected_event
                    st.session_state.timeline_trigger_dialog = True
        
        # Check work selection (only if education didn't select anything)
        if selected_work and not selected_event:
            if isinstance(selected_work, dict) and "id" in selected_work:
                event_id = selected_work["id"]
            elif isinstance(selected_work, list) and len(selected_work) > 0:
                event_id = selected_work[0]
            
            if event_id and event_id != st.session_state.last_timeline_click:
                selected_event = next((e for e in work_items if e["id"] == event_id), None)
                if selected_event:
                    st.session_state.last_timeline_click = event_id
                    st.session_state.timeline_selected_event_data = selected_event
                    st.session_state.timeline_trigger_dialog = True
        
        # Show dialog only if triggered by timeline
        if st.session_state.timeline_trigger_dialog and st.session_state.timeline_selected_event_data:
            show_timeline_dialog(st.session_state.timeline_selected_event_data)
            # Reset trigger after showing dialog
            st.session_state.timeline_trigger_dialog = False
        
        st.markdown('</div><hr>', unsafe_allow_html=True)
