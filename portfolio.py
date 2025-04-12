import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
from datetime import datetime
from streamlit_timeline import st_timeline

# Set page config for wide layout and custom title
st.set_page_config(page_title="Dajinder Singh | Data-Driven Portfolio", layout="wide", page_icon="📊")

# Custom CSS for styling (Windsor blue/gold theme)
st.markdown("""
    <style>
    .main {background-color: #F5F6F5;}
    .stSidebar {background-color: #679afa;}
    .stButton>button {background-color: #FFC107; color: #003087; border-radius: 5px;}
    .stTitle {color: #003087;}
    .card {background-color: #FFFFFF; padding: 15px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);}
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Home", "Skills", "Projects", "Timeline", "Achievements", "Blog"])

# Theme toggle
# theme = st.sidebar.selectbox("Theme", ["Light", "Dark"])
# if theme == "Dark":
#     st.markdown("<style>.main {background-color: #1E1E1E; color: #FFFFFF;} .card {background-color: #2A2A2A;}</style>", unsafe_allow_html=True)

# Sample data based on resume
skills_data = {
    "Category": ["Data Analysis", "Data Analysis", "Tools", "Tools", "Tools", "Tools", "Database", "Database", "Programming", "Programming", "Project Management"],
    "Skill": ["Excel", "Qlik Sense", "Snowflake", "Salesforce", "Streamlit", "JIRA", "Snowflake", "MySQL", "Python", "Java", "JIRA"],
    "Proficiency": [90, 85, 88, 80, 75, 90, 88, 80, 92, 85, 90],
    "Details": [
        "Advanced analytics and pivots", "Built client reports", "Optimized pipelines", 
        "Managed Qlik-to-SF transition", "Built portfolio apps", "Agile project tracking",
        "Pipeline design", "Query optimization", "Data pipelines & ML", "CLI apps", "Sprint planning"
    ]
}

project_data = {
    "Project": ["Agile Adoption", "Pipeline Optimization", "Qlik-to-Salesforce"],
    "Impact": ["40% efficiency increase", "Reduced runtime from 8 to 2.5 hours", "Smooth transition for 100+ reports"],
    "Year": [2024, 2023, 2023],
    "Metric": [40, 5.5, 100]  # Numeric for plotting (efficiency %, hours saved, reports)
}

# Home Section
if section == "Home":
    st.title("Hi, I'm Dajinder Singh!")
    st.markdown("""
    Master’s student in Applied Computing at University of Windsor with 4 years at ZS Associates in business analysis, 
    data engineering, and analytics. Expert in Python, Snowflake, and JIRA, driving efficiency and insights for global clients.
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://via.placeholder.com/300", caption="Your Photo")  # Replace with your image
    with col2:
        st.markdown("""
        <div class='card'>
        <h3>About Me</h3>
        Published ML research, won ZS Client Delight Award 2022. Passionate about data pipelines, Agile, and impactful solutions.
        </div>
        """, unsafe_allow_html=True)
        st.button("Download Resume", on_click=lambda: st.download_button("Download Resume", open("resume.pdf", "rb").read(), "resume.pdf"))

# Skills Section
elif section == "Skills":
    st.title("Skills Heatmap")
    df_skills = pd.DataFrame(skills_data)
    fig = px.density_heatmap(
        df_skills, x="Category", y="Skill", z="Proficiency", 
        text_auto=True, color_continuous_scale=["#003087", "#FFC107"]
    )
    fig.update_traces(hovertemplate="%{y}: %{z}% proficiency<br>%{customdata}", customdata=df_skills["Details"])
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("Click skills for details on projects and tools used.")

# Projects Section
elif section == "Projects":
    st.title("Project Impact")
    df_projects = pd.DataFrame(project_data)
    col1, col2 = st.columns(2)
    with col1:
        fig_bar = px.bar(df_projects, x="Project", y="Metric", color="Project", 
                         title="Key Metrics", color_discrete_sequence=["#003087", "#FFC107", "#1E88E5"])
        st.plotly_chart(fig_bar, use_container_width=True)
    with col2:
        fig_line = px.line(df_projects, x="Year", y="Metric", color="Project", 
                           title="Timeline of Impact", markers=True)
        st.plotly_chart(fig_line, use_container_width=True)
    st.markdown("""
    - **Agile Adoption**: Boosted efficiency by 40% using JIRA.
    - **Pipeline Optimization**: Cut runtime by 5.5 hours with Snowflake.
    - **Qlik-to-Salesforce**: Transitioned 100+ reports seamlessly.
    """)

# Timeline Section
elif section == "Timeline":
    st.title("Career Timeline")
    timeline_data = [
            {"id": 1, "content": "B.Tech, GGSIPU", "start": "2017-08-01", "group": "Education"},
            {"id": 2, "content": "Business Analyst Intern, ZS", "start": "2020-12-01", "end": "2021-06-30", "group": "Work"},
            {"id": 3, "content": "Data Engineer, ZS", "start": "2021-07-01", "end": "2023-01-31", "group": "Work"},
            {"id": 4, "content": "Senior Data Engineer, ZS", "start": "2023-01-01", "end": "2023-11-30", "group": "Work"},
            {"id": 5, "content": "Business Analyst, ZS", "start": "2023-12-01", "end": "2025-01-31", "group": "Work"},
            {"id": 6, "content": "MAC, University of Windsor", "start": "2025-01-01", "group": "Education"}
        ]
        # "groups": [{"id": "Education", "content": "Education"}, {"id": "Work", "content": "Work"}]
    # }
    timeline = st_timeline(timeline_data, groups=[], options={}, height="400px")
    # st.write(timeline)

# Achievements Section
elif section == "Achievements":
    st.title("Achievements")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='card'>
        <h3>ZS Client Delight Award 2022</h3>
        Recognized for outstanding client impact in analytics and delivery.
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='card'>
        <h3>Published Research</h3>
        Paper on ML algorithms for Hindi news classification at ICICC.
        </div>
        """, unsafe_allow_html=True)
        # st.download_button("Download Paper", data=open("paper.pdf "rb").read(), file_name="paper.pdf", key="paper")  # Replace with actual PDF