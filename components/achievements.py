import streamlit as st
import os
from datetime import datetime
import plotly.graph_objects as go

def create_milestone_timeline(milestones):
    """Create an interactive timeline visualization for milestones"""
    fig = go.Figure()
    
    # Add milestones as scatter points
    dates = [datetime.strptime(m['date'], '%Y-%m') for m in milestones]
    texts = [f"🏆 {m['title']}<br>{m['description']}" for m in milestones]
    
    fig.add_trace(go.Scatter(
        x=dates,
        y=[1] * len(dates),
        mode='markers+text',
        marker=dict(
            size=20,
            symbol='star',
            color='#FFD700',
            line=dict(color='#2C2A4A', width=2)
        ),
        text=[m['title'] for m in milestones],
        textposition='top center',
        hovertext=texts,
        hoverinfo='text'
    ))
    
    # Customize layout
    fig.update_layout(
        showlegend=False,
        hovermode='x unified',
        plot_bgcolor='white',
        yaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
        xaxis=dict(showgrid=True, gridcolor='#E5E7EB'),
        height=200,
        margin=dict(l=0, r=0, t=40, b=0)
    )
    
    return fig

def create_skill_radar(skills):
    """Create an interactive radar chart for skills/achievements"""
    fig = go.Figure()
    
    categories = list(skills.keys())
    values = list(skills.values())
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        fillcolor='rgba(29, 78, 216, 0.2)',
        line=dict(color='#1E40AF', width=2),
        hoverinfo='text',
        hovertext=[f"{cat}: {val}%" for cat, val in zip(categories, values)]
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                showticklabels=False,
                gridcolor='#E5E7EB'
            ),
            angularaxis=dict(
                gridcolor='#E5E7EB'
            ),
            bgcolor='white'
        ),
        showlegend=False,
        margin=dict(l=40, r=40, t=20, b=20),
        height=300
    )
    
    return fig

def create_impact_bar(impact_data):
    """Create an animated bar chart for impact metrics"""
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=list(impact_data.values()),
        y=list(impact_data.keys()),
        orientation='h',
        marker=dict(
            color=['#3B82F6', '#2563EB', '#1D4ED8'],
            line=dict(color='#2C2A4A', width=1)
        ),
        text=list(impact_data.values()),
        textposition='outside'
    ))
    
    fig.update_layout(
        plot_bgcolor='white',
        xaxis=dict(showgrid=True, gridcolor='#E5E7EB', zeroline=False),
        yaxis=dict(showgrid=False),
        margin=dict(l=0, r=0, t=20, b=0),
        height=200
    )
    
    return fig

def render_achievement_card(title, date, description, category, impact="", link=None):
    """Render an interactive achievement card"""
    with st.container():
        st.markdown(f"""
        <div class="achievement-card">
            <div class="achievement-header">
                <span class="achievement-category">{category}</span>
                <span class="achievement-date">{date}</span>
            </div>
            <h3>{title}</h3>
            <p>{description}</p>
            {f'<div class="achievement-impact">🎯 Impact: {impact}</div>' if impact else ''}
            {f'<a href="{link}" target="_blank" class="achievement-link">📄 View Publication</a>' if link else ''}
        </div>
        """, unsafe_allow_html=True)

def render():
    """Render the achievements section with interactive elements"""
    
    # Add custom CSS
    st.markdown("""
    <style>
    .achievement-card {
        background: white;
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease;
    }
    
    .achievement-card:hover {
        transform: translateY(-5px);
    }
    
    .achievement-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
    }
    
    .achievement-category {
        background: #EFF6FF;
        color: #2563EB;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 14px;
    }
    
    .achievement-date {
        color: #6B7280;
        font-size: 14px;
    }
    
    .achievement-impact {
        margin-top: 10px;
        padding: 8px;
        background: #F0FDF4;
        color: #059669;
        border-radius: 6px;
        font-size: 14px;
    }
    
    .achievement-link {
        display: inline-block;
        margin-top: 10px;
        color: #2563EB;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.2s ease;
    }
    
    .achievement-link:hover {
        color: #1D4ED8;
    }
    
    .milestone-card {
        text-align: center;
        padding: 20px;
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 10px 0;
    }
    
    .milestone-number {
        font-size: 32px;
        font-weight: bold;
        color: #2563EB;
        margin-bottom: 8px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div id="achievements">', unsafe_allow_html=True)
        st.title("🏆 Achievements & Recognition")
        
        # Key Milestones Cards
        milestone_cols = st.columns(3)
        with milestone_cols[0]:
            st.markdown("""
            <div class="milestone-card">
                <div class="milestone-number">3.5+</div>
                <div>Years Experience</div>
            </div>
            """, unsafe_allow_html=True)
        with milestone_cols[1]:
            st.markdown("""
            <div class="milestone-card">
                <div class="milestone-number">3+</div>
                <div>Major Projects</div>
            </div>
            """, unsafe_allow_html=True)
        with milestone_cols[2]:
            st.markdown("""
            <div class="milestone-card">
                <div class="milestone-number">3+</div>
                <div>Awards and Client Recognition</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Achievement Timeline
        # st.markdown("### 🌟 Achievement Timeline")
        # milestones = [
        #     {
        #         'title': 'ZS Client Delight Award',
        #         'date': '2022-12',
        #         'description': 'Recognized for outstanding client impact'
        #     },
        #     {
        #         'title': 'Research Publication',
        #         'date': '2023-03',
        #         'description': 'ML paper published at ICICC'
        #     },
        #     {
        #         'title': 'Senior Data Engineer Promotion',
        #         'date': '2023-01',
        #         'description': 'Promoted for exceptional performance'
        #     },
        #     {
        #         'title': 'Master\'s Program',
        #         'date': '2025-01',
        #         'description': 'Started MAC at UWindsor'
        #     }
        # ]
        # timeline_fig = create_milestone_timeline(milestones)
        # st.plotly_chart(timeline_fig, use_container_width=True)
        
        # Tabs for different achievement categories
        achievement_tabs = st.tabs(["🎯 Professional", "📚 Academic", "🔬 Research"])
        
        with achievement_tabs[0]:
            # Professional Achievements
            render_achievement_card(
                "ZS Client Delight Award 2022",
                "December 2022",
                "Recognized for outstanding client impact in analytics and delivery, specifically for optimizing data pipelines and improving process efficiency.",
                "Professional Excellence",
                "40% improvement in process efficiency"
            )
            
            render_achievement_card(
                "Senior Data Engineer Promotion",
                "January 2023",
                "Promoted to Senior Data Engineer role for exceptional performance in data pipeline optimization and team leadership.",
                "Career Growth",
                "Led team of 5 engineers"
            )
        
        with achievement_tabs[1]:
            # Academic Achievements
            render_achievement_card(
                "Master of Applied Computing",
                "2025-Present",
                "Pursuing MAC at University of Windsor with focus on AI and ML.",
                "Higher Education",
                "Current GPA: 3.2/4.0"
            )
            
            render_achievement_card(
                "B.Tech in Information Technology",
                "2017-2021",
                "Completed B.Tech from GGSIPU with distinction.",
                "Bachelor's Degree",
                "GPA: 8.7/10.0"
            )
        
        with achievement_tabs[2]:
            # Research Achievements
            render_achievement_card(
                "ML Research Publication",
                "March 2023",
                "Published research paper on ML algorithms for Hindi news classification at ICICC conference.",
                "Research",
                "Novel approach with 92% accuracy",
                "https://link.springer.com/chapter/10.1007/978-981-16-2597-8_27"
            )
            
            # Skills radar chart
            # st.markdown("### 💡 Research Skills")
            # research_skills = {
            #     'ML Algorithms': 85,
            #     'Data Analysis': 90,
            #     'Research Methods': 80,
            #     'Paper Writing': 75,
            #     'Experimentation': 85
            # }
            # skills_fig = create_skill_radar(research_skills)
            # st.plotly_chart(skills_fig, use_container_width=True)
            
            # # Impact metrics
            # st.markdown("### 📊 Research Impact")
            # impact_data = {
            #     'Citations': 15,
            #     'Conference Presentations': 2,
            #     'Projects Completed': 5
            # }
            # impact_fig = create_impact_bar(impact_data)
            # st.plotly_chart(impact_fig, use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)