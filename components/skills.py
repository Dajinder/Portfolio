import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.data import get_skills_data

# def render():
#     """Render the skills section"""
    
#     # Initialize skills session state (separate from timeline)
#     if "selected_skill_category" not in st.session_state:
#         st.session_state.selected_skill_category = "Programming"
    
#     # Skills Heatmap
#     with st.container():
#         st.markdown('<div id="skills" class="py-8">', unsafe_allow_html=True)
#         st.title("Skills Heatmap")
        
#         df_skills = pd.DataFrame(get_skills_data())
#         fig = px.density_heatmap(
#             df_skills, x="Category", y="Skill", z="Proficiency", 
#             text_auto=True, color_continuous_scale=["#003087", "#FFC107"]
#         )
#         fig.update_traces(
#             hovertemplate="%{y}: %{z}% proficiency<br>%{customdata}", 
#             customdata=df_skills["Details"]
#         )
#         st.plotly_chart(fig, use_container_width=True)
#         st.markdown(
#             '<p class="text-center text-gray-600 mt-4">Click skills for details on projects and tools used.</p>', 
#             unsafe_allow_html=True
#         )
#         st.markdown('</div><hr>', unsafe_allow_html=True)
    
#     # Skills Radar
#     render_skills_radar()

def render_skills_radar():
    """Render skills radar chart"""
    with st.container():
        st.markdown('<div id="skill" class="py-8">', unsafe_allow_html=True)
        st.title("Skills Radar")
        
        skills = {
            "Tools & Tech": {
                "Palantir Foundry": (85, "Collaborative data ecosystem"),
                "IICS(Cloud)": (75, "Cloud data integration"),
                "Qlik Sense": (80, "Self-service BI"),
                "Salesforce": (70, "CRM workflows"),
                "Streamlit": (85, "Python web apps"),
                "Autosys": (60, "Job automation"),
                "Windchill": (55, "Product lifecycle management")
            },
            "Data Analysis": {
                "Excel (Advanced)": (90, "Advanced spreadsheet analytics & visualization"),
                "Palantir Foundry (Contour)": (85, "Big data integration and transformation"),
                "Qlik Sense": (80, "BI dashboard development and analysis")
            },
            "Database": {
                "Teradata": (75, "Enterprise data warehouse"),
                "Snowflake": (80, "Cloud-native DB"),
                "Oracle": (70, "Relational DBMS"),
                "MySQL": (65, "Open-source SQL DB")
            },
            "Programming": {
                "Python": (90, "Scripting, automation, and data science"),
                "Java": (80, "Object-oriented programming"),
                "Shell Script": (70, "Linux automation")
            },
            "Project Mgmt": {
                "JIRA": (65, "Agile project tracking")
            }
        }
        
        # Use a unique key for the selectbox to avoid conflicts
        category = st.selectbox(
            "🧩 Select a Skill Category", 
            list(skills.keys()),
            key="skill_category_selector",
            index=list(skills.keys()).index(st.session_state.selected_skill_category)
        )
        
        # Update session state
        st.session_state.selected_skill_category = category
        
        tools = list(skills[category].keys())
        scores = [skills[category][tool][0] for tool in tools]
        
        # Loop back for closure
        tools += [tools[0]]
        scores += [scores[0]]
        
        fig = go.Figure(
            data=[
                go.Scatterpolar(
                    r=scores,
                    theta=tools,
                    fill='toself',
                    name=category,
                    line=dict(color="#3bf683"),
                    hoverinfo='text',
                    text=[f"{t}: {s}%" for t, s in zip(tools, scores)]
                )
            ],
            layout=go.Layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                showlegend=False,
                margin=dict(l=5, r=5, t=50, b=50)
            )
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div><hr>', unsafe_allow_html=True)
