import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.data import get_project_data
from utils.api import get_github_data

def create_impact_meter(value, max_value=100):
    """Create an animated impact meter"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [None, max_value]},
            'bar': {'color': "#1E88E5"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#2C2A4A",
            'steps': [
                {'range': [0, max_value/2], 'color': '#FFE0B2'},
                {'range': [max_value/2, max_value], 'color': '#BBDEFB'}
            ],
        }
    ))
    fig.update_layout(height=200, margin=dict(l=10, r=10, t=30, b=10))
    return fig

def create_tech_bubble(technologies):
    """Create an interactive bubble chart for technologies used"""
    tech_data = []
    for tech, details in technologies.items():
        tech_data.append({
            'Technology': tech,
            'Usage': details['usage'],
            'Category': details['category'],
            'Experience': details['experience']
        })
    
    df_tech = pd.DataFrame(tech_data)
    fig = px.scatter(df_tech, 
                    x='Usage', 
                    y='Experience',
                    size='Usage',
                    color='Category',
                    hover_name='Technology',
                    text='Technology',
                    color_discrete_sequence=px.colors.qualitative.Set3)
    
    fig.update_traces(textposition='top center')
    fig.update_layout(height=400)
    return fig

def render_project_card(title, description, metrics, tech_stack, github_link=None):
    """Render an interactive project card"""
    with st.expander(f"🚀 {title}", expanded=False):
        cols = st.columns([2, 1])
        with cols[0]:
            st.markdown(f"### {title}")
            st.markdown(description)
            st.markdown("#### 💻 Tech Stack")
            tech_html = " ".join([f"<span class='tech-badge {tech.lower()}'>{tech}</span>" for tech in tech_stack])
            st.markdown(f"<div class='tech-stack'>{tech_html}</div>", unsafe_allow_html=True)
        
        with cols[1]:
            for metric_name, value in metrics.items():
                st.metric(metric_name, value)
        
        if github_link:
            st.markdown(f"[View on GitHub]({github_link}) 👨‍💻")

def render():
    """Render the projects section"""
    
    st.markdown("""
    <style>
    .tech-stack {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin: 10px 0;
    }
    .tech-badge {
        background-color: #E3F2FD;
        color: #1E88E5;
        padding: 4px 12px;
        border-radius: 16px;
        font-size: 14px;
        transition: all 0.3s ease;
    }
    .tech-badge:hover {
        transform: translateY(-2px);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .github-activity {
        background: #F8F9FA;
        border-radius: 8px;
        padding: 16px;
        margin: 16px 0;
        border-left: 4px solid #1E88E5;
    }
    .impact-number {
        font-size: 24px;
        font-weight: bold;
        color: #1E88E5;
    }
    .project-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 16px;
        margin: 16px 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div id="projects">', unsafe_allow_html=True)
        
        # Header with dynamic tabs
        st.title("🚀 Projects & Impact")
        tabs = st.tabs(["📊 Impact Overview", "🎯 Project Details", "🔄 GitHub Activity"])
        
        # Tab 1: Impact Overview
        with tabs[0]:
            metrics_cols = st.columns(3)
            with metrics_cols[0]:
                st.markdown("### 🎯 Process Optimization")
                fig = create_impact_meter(40)
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("<p class='impact-number'>40% Efficiency Boost</p>", unsafe_allow_html=True)
            
            with metrics_cols[1]:
                st.markdown("### ⚡ Performance Gain")
                fig = create_impact_meter(68)
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("<p class='impact-number'>68% Runtime Reduction</p>", unsafe_allow_html=True)
            
            with metrics_cols[2]:
                st.markdown("### 📈 User Adoption")
                fig = create_impact_meter(85)
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("<p class='impact-number'>85% User Satisfaction</p>", unsafe_allow_html=True)
            
            # Technology Bubble Chart
            st.markdown("### 🔧 Technology Ecosystem")
            tech_data = {
                'Python': {'usage': 90, 'category': 'Programming', 'experience': 95},
                'Snowflake': {'usage': 75, 'category': 'Data', 'experience': 85},
                'JIRA': {'usage': 80, 'category': 'Tools', 'experience': 90},
                'Git': {'usage': 85, 'category': 'Tools', 'experience': 88},
                'SQL': {'usage': 85, 'category': 'Data', 'experience': 92},
                'Salesforce': {'usage': 70, 'category': 'Platform', 'experience': 75}
            }
            tech_bubble_chart = create_tech_bubble(tech_data)
            st.plotly_chart(tech_bubble_chart, use_container_width=True)
        
        # Tab 2: Project Details
        with tabs[1]:
            projects = [
                {
                    'title': 'Data Pipeline Optimization',
                    'description': 'Redesigned and optimized data pipelines for Incentive Compensation data, reducing process runtime from 8 hours to 2.5 hours.',
                    'metrics': {
                        'Runtime Reduction': '5.5 hrs',
                        'Data Volume': '1TB+',
                        'ROI': '300%'
                    },
                    'tech_stack': ['Python', 'Snowflake', 'Informatica', 'Shell']
                },
                {
                    'title': 'Salesforce Migration',
                    'description': 'Led the transition of 100+ reports from Qlik Sense to Salesforce CRM Platform, ensuring data consistency and user adoption.',
                    'metrics': {
                        'Reports Migrated': '100+',
                        'User Adoption': '95%',
                        'Time Saved': '20 hrs/week'
                    },
                    'tech_stack': ['Salesforce', 'Qlik Sense', 'SQL', 'JavaScript']
                }
            ]
            
            for project in projects:
                render_project_card(**project)
        
        # Tab 3: GitHub Activity
        with tabs[2]:
            st.markdown("### 👨‍� Recent GitHub Activity")
            with st.spinner("Fetching latest GitHub activity..."):
                github_data = get_github_data("Dajinder")
                
            if not github_data.empty:
                activity_cols = st.columns(2)
                for idx, row in github_data.iterrows():
                    with activity_cols[idx % 2]:
                        repo_name = row["Repo"].split("/")[1] if "/" in row["Repo"] else row["Repo"]
                        st.markdown(f"""
                        <div class='github-activity'>
                            <h4>{repo_name}</h4>
                            <p>🎯 {row['Type']}</p>
                            <p>�️ {row['Date']}</p>
                            <a href='https://github.com/{row['Repo']}' target='_blank'>View Repository 🔗</a>
                        </div>
                        """, unsafe_allow_html=True)
            else:
                st.warning("⚠️ No recent GitHub activity found. Please check back later!")
        
        st.markdown('</div>', unsafe_allow_html=True)
