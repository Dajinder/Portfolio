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
    """Render skills radar chart with enhanced interactivity"""
    with st.container():
        st.markdown('<div id="skills" class="py-8">', unsafe_allow_html=True)
        
        # Add custom CSS for animations and styling
        st.markdown("""
        <style>
        .skills-header {
            text-align: center;
            margin-bottom: 2rem;
            animation: fadeIn 0.8s ease-in;
        }
        
        .skill-category-selector {
            margin-bottom: 2rem;
            padding: 1rem;
            background: linear-gradient(135deg, #f6f8fa 0%, #ffffff 100%);
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .skill-info-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-top: 1rem;
            transition: all 0.3s ease;
        }
        
        .skill-info-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
        
        .proficiency-meter {
            height: 8px;
            background: #e9ecef;
            border-radius: 4px;
            overflow: hidden;
            margin: 8px 0;
        }
        
        .proficiency-fill {
            height: 100%;
            background: linear-gradient(90deg, #3bf683 0%, #4CAF50 100%);
            border-radius: 4px;
            transition: width 1s ease-in-out;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .skill-tag {
            display: inline-block;
            padding: 4px 12px;
            background: #e3f2fd;
            color: #1976d2;
            border-radius: 15px;
            margin: 4px;
            font-size: 0.9rem;
            transition: all 0.2s ease;
        }
        
        .skill-tag:hover {
            background: #1976d2;
            color: white;
            transform: translateY(-2px);
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Header with animation
        # st.markdown('<div class="skills-header"><h1>💫 Skills Radar</h1></div>', unsafe_allow_html=True)
        st.title("💫 Skills Radar")
        # Define skills with consistent data structure
        skills = {
            "Tools & Tech": {
                "Palantir Foundry": {
                    "proficiency": 85,
                    "description": "Collaborative data ecosystem",
                    "tags": ["Data Integration", "Pipeline Design", "Data Modeling"]
                },
                "IICS(Cloud)": {
                    "proficiency": 75,
                    "description": "Cloud data integration",
                    "tags": ["ETL", "Cloud Computing", "Data Migration"]
                },
                "Qlik Sense": {
                    "proficiency": 80,
                    "description": "Self-service BI",
                    "tags": ["Dashboard Design", "Data Visualization", "Analytics"]
                },
                "Salesforce": {
                    "proficiency": 70,
                    "description": "CRM workflows",
                    "tags": ["CRM", "Process Automation", "Reporting"]
                },
                "Streamlit": {
                    "proficiency": 85,
                    "description": "Python web apps",
                    "tags": ["Web Development", "Data Apps", "UI/UX"]
                },
                "Autosys": {
                    "proficiency": 60,
                    "description": "Job automation",
                    "tags": ["Scheduling", "Process Automation", "Monitoring"]
                },
                "Windchill": {
                    "proficiency": 55,
                    "description": "Product lifecycle management",
                    "tags": ["PLM", "Document Management", "Workflow"]
                }
            },
            "Data Analysis": {
                "Excel (Advanced)": {
                    "proficiency": 90,
                    "description": "Advanced spreadsheet analytics & visualization",
                    "tags": ["Data Analysis", "Visualization", "Business Intelligence"]
                },
                "Palantir Foundry (Contour)": {
                    "proficiency": 85,
                    "description": "Big data integration and transformation",
                    "tags": ["Data Integration", "ETL", "Data Analysis"]
                },
                "Qlik Sense": {
                    "proficiency": 80,
                    "description": "BI dashboard development and analysis",
                    "tags": ["Business Intelligence", "Dashboard Design", "Analytics"]
                }
            },
            "Database": {
                "Teradata": {
                    "proficiency": 75,
                    "description": "Enterprise data warehouse",
                    "tags": ["Data Warehouse", "SQL", "Performance Tuning"]
                },
                "Snowflake": {
                    "proficiency": 80,
                    "description": "Cloud-native DB",
                    "tags": ["Cloud Database", "Data Warehouse", "SQL"]
                },
                "Oracle": {
                    "proficiency": 70,
                    "description": "Relational DBMS",
                    "tags": ["RDBMS", "SQL", "Database Administration"]
                },
                "MySQL": {
                    "proficiency": 65,
                    "description": "Open-source SQL DB",
                    "tags": ["RDBMS", "SQL", "Open Source"]
                }
            },
            "Programming": {
                "Python": {
                    "proficiency": 90,
                    "description": "Scripting, automation, and data science",
                    "tags": ["Data Science", "Automation", "Web Development"]
                },
                "Java": {
                    "proficiency": 80,
                    "description": "Object-oriented programming",
                    "tags": ["OOP", "Backend", "Applications"]
                },
                "Shell Script": {
                    "proficiency": 70,
                    "description": "Linux automation",
                    "tags": ["Automation", "Linux", "Scripting"]
                }
            },
            "Project Mgmt": {
                "JIRA": {
                    "proficiency": 65,
                    "description": "Agile project tracking",
                    "tags": ["Agile", "Project Management", "Scrum"]
                }
            }
        }
        
        # Category and filter controls with enhanced styling
        col1, col2, col3 = st.columns([2, 2, 1])
        
        with col1:
            st.markdown('<div class="skill-category-selector">', unsafe_allow_html=True)
            category = st.selectbox(
                "🧩 Select a Skill Category", 
                list(skills.keys()),
                key="skill_category_selector",
                index=list(skills.keys()).index(st.session_state.selected_skill_category)
            )
        
        with col2:
            sort_by = st.radio(
                "Sort skills by:",
                ["Name", "Proficiency"],
                horizontal=True,
                key="skills_sort"
            )
            
        with col3:
            min_proficiency = st.slider(
                "Min. Proficiency",
                0, 100, 0,
                step=10,
                key="min_proficiency"
            )
        
        # Update session state
        st.session_state.selected_skill_category = category
        
        # Initialize or update clicked skill in session state
        if 'clicked_skill' not in st.session_state:
            st.session_state.clicked_skill = None
        
        # Filter and sort skills
        filtered_skills = {
            k: v for k, v in skills[category].items() 
            if v["proficiency"] >= min_proficiency
        }
        
        if sort_by == "Name":
            sorted_skills = dict(sorted(filtered_skills.items()))
        else:  # sort by Proficiency
            sorted_skills = dict(sorted(
                filtered_skills.items(),
                key=lambda x: x[1]["proficiency"],
                reverse=True
            ))
        
        tools = list(sorted_skills.keys())
        scores = [sorted_skills[tool]["proficiency"] for tool in tools]
        
        if not tools:
            st.warning("No skills match the selected criteria. Try adjusting the filters.")
            return
        
        # Loop back for closure in radar chart
        tools_radar = tools + [tools[0]]
        scores_radar = scores + [scores[0]]
        
        # Create enhanced radar chart
        fig = go.Figure()
        
        # Add background circle for reference
        fig.add_trace(go.Scatterpolar(
            r=[100]*len(tools_radar),
            theta=tools_radar,
            fill='toself',
            name='Max',
            fillcolor='rgba(242, 242, 242, 0.3)',
            line=dict(color='rgba(200, 200, 200, 0.2)'),
            showlegend=False
        ))
        
        # Add main skills trace with gradient fill
        fig.add_trace(go.Scatterpolar(
            r=scores_radar,
            theta=tools_radar,
            fill='toself',
            name=category,
            line=dict(color='#3bf683', width=2),
            fillcolor='rgba(59, 246, 131, 0.2)',
            hoverinfo='text',
            text=[f"{t}: {s}%<br>Click for details" for t, s in zip(tools_radar, scores_radar)]
        ))
        
        # Customize layout
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    tickfont=dict(size=10),
                    ticksuffix='%',
                    gridcolor='rgba(0, 0, 0, 0.1)',
                    angle=45
                ),
                angularaxis=dict(
                    tickfont=dict(size=11),
                    gridcolor='rgba(0, 0, 0, 0.1)'
                ),
                bgcolor='white'
            ),
            showlegend=False,
            margin=dict(l=20, r=20, t=40, b=40),
            height=500,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        
        # Initialize session state for selected skill if not exists
        if 'selected_skill_name' not in st.session_state:
            st.session_state.selected_skill_name = None

        # Display the chart with click events
        fig.update_layout(
            clickmode='event+select'
        )
        
        # Display the chart
        clicked = plotly_chart_with_events = st.plotly_chart(
            fig,
            use_container_width=True,
            key='skills_radar_chart'
        )
        
        # Add a selectbox below the chart for mobile-friendly interaction
        st.markdown("### 📱 Select a skill to view details")
        selected_skill = st.selectbox(
            "Choose a skill",
            options=tools,
            key="skill_selector",
            label_visibility="collapsed"
        )
        
        # Update selected skill in session state
        st.session_state.selected_skill_name = selected_skill
        
        # Show skill details if one is selected
        if st.session_state.selected_skill_name and st.session_state.selected_skill_name in skills[category]:
            skill_info = skills[category][st.session_state.selected_skill_name]
            st.markdown(f"""
            <div class="skill-info-card">
                <h3>{st.session_state.selected_skill_name}</h3>
                <div class="proficiency-meter">
                    <div class="proficiency-fill" style="width: {skill_info['proficiency']}%;"></div>
                </div>
                <p><strong>Proficiency:</strong> {skill_info['proficiency']}%</p>
                <p><strong>Description:</strong> {skill_info['description']}</p>
                <div style="margin-top: 10px;">
                    {''.join([f'<span class="skill-tag">{tag}</span>' for tag in skill_info['tags']])}
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div><hr>', unsafe_allow_html=True)
