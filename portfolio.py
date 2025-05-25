import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from datetime import datetime
from streamlit_timeline import st_timeline
import os
from datetime import date

import plotly.graph_objects as go


# Set page config
st.set_page_config(page_title="Dajinder | Data-Driven Portfolio", layout="wide", page_icon="📊")

# Include Tailwind CSS via CDN and custom styles
st.markdown("""
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        html { scroll-behavior: smooth; }
        /* Override Streamlit button styles */
        .stButton>button {
            background-color: #FFC107;
            color: #003087;
            border-radius: 0.375rem;
            padding: 0.5rem 1rem;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #FFD700;
        }
        /* Override Streamlit title color */
        .stTitle, h1 {
            color: #003087 !important;
        }
        /* Ensure hr styling */
        hr {
            border-top: 1px solid #003087;
            margin: 1rem 0;
        }
    </style>
""", unsafe_allow_html=True)

# Configure Tailwind with custom colors
st.markdown("""
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'windsor-blue': '#003087',
                        'windsor-gold': '#FFC107',
                    }
                }
            }
        }
    </script>
""", unsafe_allow_html=True)


# Resume-based data
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
    "Metric": [40, 5.5, 100]
}



# Experience data for timeline
experience_data = [
    {
        "Task": "Business Technology Associate Consultant",
        "Start": "2023-12-01",
        "End": "2025-01-31",
        "Company": "ZS Associates",
        "Details": [
            "Led business analysis for requirement gathering, documentation, testing, and project delivery for major pharmaceutical clients.",
            "Authored User Requirement Specifications (URS), Functional Requirement Specifications (FRS), and User Acceptance Testing (UAT) documentation.",
            "Implemented Agile methodology using JIRA, resulting in a 40% increase in project efficiency."
        ]
    },
    {
        "Task": "Senior Data Engineer",
        "Start": "2023-01-01",
        "End": "2023-11-30",
        "Company": "ZS Associates",
        "Details": [
            "Designed and optimized data pipelines for compensation data using Informatica and Snowflake; automated triggers with Autosys and shell scripts.",
            "Reduced process runtime from 8 hours to 2.5 hours, enhancing overall efficiency.",
            "Managed migration of data pipelines and tables between environments using Windchill."
        ]
    },
    {
        "Task": "Data Engineer",
        "Start": "2021-07-01",
        "End": "2023-01-31",
        "Company": "ZS Associates",
        "Details": [
            "Developed and maintained reports on Qlik Sense and Salesforce; facilitated transition from Qlik to Salesforce.",
            "Conducted data quality analysis with SQL and Excel."
        ]
    },
    {
        "Task": "Business Analyst Intern",
        "Start": "2020-12-01",
        "End": "2021-06-30",
        "Company": "ZS Associates",
        "Details": [
            "Created and managed reports using Qlik Sense; delivered weekly development and operational reports to clients.",
            "Performed quality analysis of data with SQL and Excel."
        ]
    }
]




# GitHub API
@st.cache_data(ttl=3600)
def get_github_data(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            events = response.json()
            return pd.DataFrame([
                {
                    "Type": event["type"],
                    "Repo": event["repo"]["name"],
                    "Date": datetime.strptime(event["created_at"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d")
                }
                for event in events[:10]
            ])
        return pd.DataFrame({"Type": ["N/A"], "Repo": ["N/A"], "Date": ["N/A"]})
    except:
        return pd.DataFrame({"Type": ["N/A"], "Repo": ["N/A"], "Date": ["N/A"]})



# Custom CSS to manage responsive styles
st.markdown("""
<style>
/* Full navbar styles */
            .nav-heading {
            color: white;
            }
.navbar {
    background-color: #2C2A4A; /* windsor-blue */
    padding: 1rem;
    position: fixed;
    left: 0;
    width: 100%;
    margin-top: 50px;
    top: 0;
    z-index: 50;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* Navbar links (desktop) */
.nav-links {
    display: flex;
    gap: 1.5rem;
}

.nav-links a {
    color: white;
    text-decoration: none;
    font-weight: bold;
    padding: 5px
}

.nav-links a:hover {
    color: #FFD700; /* windsor-gold */
}

/* Hamburger (hidden on desktop) */
.hamburger {
    display: none;
    font-size: 1.5rem;
    color: white;
    cursor: pointer;
    background: none;
    border: none;
}

/* Mobile menu */
.mobile-menu {
    display: none;
    flex-direction: column;
    gap: 1rem;
    margin-top: 1rem;
}

/* Responsive behavior */
@media (max-width: 768px) {
    .nav-links {
        display: none;
    }
    .hamburger {
        display: block;
    }
    .mobile-menu.show {
        display: flex;
    }
}
</style>
""", unsafe_allow_html=True)

# Toggle state for hamburger
if "menu_open" not in st.session_state:
    st.session_state.menu_open = False

def toggle_menu():
    st.session_state.menu_open = not st.session_state.menu_open

# Navbar container
st.markdown(f"""
<div class="navbar">
    <div class="nav-heading text-white font-bold text-lg">Dajinder</div>
    <div class="nav-links">
        <a href="#home">Home</a>
        <a href="#experience">Career Timeline</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#timeline">Timeline</a>
        <a href="#achievements">Achievements</a>
        <a href="#blog">Blog</a>
    </div>
    <button class="hamburger" onclick="document.getElementById('menu').classList.toggle('show')">☰</button>
</div>

<div id="menu" class="mobile-menu {'show' if st.session_state.menu_open else ''}">
    <a href="#home">Home</a>
    <a href="#experience">Career Timeline</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
    <a href="#timeline">Timeline</a>
    <a href="#achievements">Achievements</a>
    <a href="#blog">Blog</a>
</div>
""", unsafe_allow_html=True)

# Toggle button in Streamlit (triggers re-render)
st.button("Menu", on_click=toggle_menu, key="real_toggle", help="Only used to control state; can be hidden")






# Home Section
with st.container():
    st.markdown('<div id="home" class="py-8">', unsafe_allow_html=True)
    st.title("Hi, I'm Dajinder!")
    st.markdown("""
    Master’s student in Applied Computing at University of Windsor with 4 years at ZS Associates in business analysis, 
    data engineering, and analytics. Expert in Python, Snowflake, and JIRA, driving efficiency and insights for global clients.
    """)
    col1, col2 = st.columns([1, 1], gap="medium")
    with col1:
        st.image("https://via.placeholder.com/300", caption="Your Photo", use_container_width=True)
    with col2:
        st.markdown("""
        <div class="bg-white p-4 rounded-lg shadow-lg">
            <h3 class="text-xl font-semibold text-windsor-blue mb-2">About Me</h3>
            <p class="text-gray-700">Published ML research, won ZS Client Delight Award 2022. Passionate about data pipelines, Agile, and impactful solutions.</p>
        </div>
        """, unsafe_allow_html=True)
        resume_path = "resume.pdf"
        if os.path.exists(resume_path):
            st.download_button("Download Resume", data=open(resume_path, "rb").read(), file_name="resume.pdf", key="resume")
        else:
            st.warning("Please add resume.pdf to the folder.")
    st.markdown('</div><hr>', unsafe_allow_html=True)



# Timeline data with detailed descriptions
timeline_data = [
    {
        "id": 1, "content": "B.Tech (Information Technology) , GGSIPU", "start": "Aug 2017", "end": "June 2021", "group": "Education",
        "title": "Completed Bachelors of Technology in Information Technology from GGSIPU with GPA of 8 out of 10.",
        "style": "background-color: #cce5ff; border: 2px solid #3399ff;"
    },
    {
        "id": 2, "content": "Business Analyst Intern, ZS", "start": "Dec 2020", "end": "May 2021", "group": "Work",
        "title": "Created and managed reports using Qlik Sense for Sales and Field Force data of Pharma Clients. Delivered weekly development and operational reports to clients."
                 "Performed quality analysis of data with SQL and Excel.",
        "style": "background-color: #ffe5b4; border: 2px solid #ff9900;"
    },
    {
        "id": 3, "content": "Business Technology Associate, ZS", "start": "Jun 2021", "end": "Dec 2022",  "group": "Work",
        "title": "Performed Development, Testing and Deployment of reports on Qlik Sense and Salesforce. Facilitated transition of reports from Qlik Sense to Salesforce CRM Platform."
                 "Conducted data quality analysis and documentation such as Requirement Gathering, BRD, FRS etc.",
        "style": "background-color: #ffe5b4; border: 2px solid #ff9900;"
    },
    {
        "id": 4, "content": "Business Technology Associate, ZS", "start": "Jan 2023",  "end": "Nov 2023", "group": "Work",
        "title": "Designed and optimized data pipelines for Incentive Compensation data for Sales using Informatica (IICS) and Snowflake. Automated triggers with Autosys and shell scripts."
                 "Reduced process runtime from 8 hours to 2.5 hours, enhancing overall efficiency."
                 "Managed deployment of data pipelines, tables and other dependencies between environments using Windchill tool.",
        "style": "background-color: #ffe5b4; border: 2px solid #ff9900;"
    },
    {
        "id": 5, "content": "Business Technology Associate Consultant, ZS", "start": "Dec 2023", "end":"Jan 2025",  "group": "Work",
        "title": "Led business analysis for requirement gathering, documentation, testing, and project delivery for Pricing project of major pharmaceutical clients."
                 "Authored User Requirement Specifications (URS), Functional Requirement Specifications (FRS), and User Acceptance Testing (UAT) documentation."
                 "Implemented Agile methodology using JIRA, resulting in a 40% increase in project efficiency."
                 "Promoted to Business Technology Associate Consultant Role",
        "style": "background-color: #ffe5b4; border: 2px solid #ff9900;"
    },
    {
        "id": 6, "content": "Masters in Applied Computing, University of Windsor", "start": "2025-01-01", "end": "2026-06-01", "group": "Education",
        "title": "Pursuing Master of Applied Computing to upskill in AI and ML.",
        "style": "background-color: #cce5ff; border: 2px solid #3399ff;"
    }
]


# Initialize session state
if "selected_edu_event" not in st.session_state:
    st.session_state.selected_edu_event = None
if "selected_work_event" not in st.session_state:
    st.session_state.selected_work_event = None

# Dialog for Education
@st.dialog("🎓 Education Details")
def show_education_dialog():
    event = st.session_state.selected_edu_event
    st.write(event["content"])
    st.write(event["title"])
    st.write(f"**Start:** {event['start']}")
    if "end" in event:
        st.write(f"**End:** {event['end']}")
    # if st.button("Close"):
    #     st.session_state.selected_edu_event = None
    #     st.rerun()

# Dialog for Work
@st.dialog("💼 Work Details")
def show_work_dialog():
    event = st.session_state.selected_work_event
    st.write(event["content"])
    st.write(event["title"])
    st.write(f"**Start:** {event['start']}")
    if "end" in event:
        st.write(f"**End:** {event['end']}")
    # if st.button("Close"):
    #     st.session_state.selected_work_event = None
    #     st.rerun()


with st.container():
    st.markdown('<div id="experience" class="py-8">', unsafe_allow_html=True)
    # Timeline display
    st.title("Career Timeline")


    # Separate by group
    education_items = [i for i in timeline_data if i["group"] == "Education"]
    work_items = [i for i in timeline_data if i["group"] == "Work"]

    

    # Work timeline
    st.subheader("💼 Professional Timeline: ZS Associates PVT LTD.")
    selected_work = st_timeline(
        items=work_items,
        groups=[],
        options={"clickToUse": True},
        height="200px"
    )
    

    # Education timeline
    st.subheader("🎓 Education Timeline")
    selected_edu = st_timeline(
        items=education_items,
        groups=[],
        options={"clickToUse": True},
        height="150px"
    )


    # Show dialog if item selected
    if selected_edu and "id" in selected_edu:
        event = next((e for e in education_items if e["id"] == selected_edu["id"]), None)
        if event:
            st.session_state.selected_edu_event = event
            show_education_dialog()

    elif selected_work and "id" in selected_work:
        event = next((e for e in work_items if e["id"] == selected_work["id"]), None)
        if event:
            st.session_state.selected_work_event = event
            show_work_dialog()

    # Show dialog if an event is selected
    # if st.session_state.dialog_event:
    #     show_event_dialog()


#===============================================

# st.markdown('<div id="timeline" class="py-8">', unsafe_allow_html=True)
# st.subheader("📆 Career & Education Timeline")

# st.markdown("""
# <style>
#     .timeline-wrapper {
#         overflow-x: auto;
#         -webkit-overflow-scrolling: touch;
#     }
#     .timeline-wrapper > iframe {
#         width: 100% !important;
#         min-width: 600px;
#         max-width: 100%;
#     }

#     @media (max-width: 768px) {
#         .timeline-wrapper > iframe {
#             min-width: 100% !important;
#             height: 500px !important;
#         }
#     }
# </style>
# <div class="timeline-wrapper">
# """, unsafe_allow_html=True)

# st_timeline(timeline_data, groups=[{"id": "Education", "content": "Education"}, {"id": "Work", "content": "Work"}])

# st.markdown("</div>", unsafe_allow_html=True)




#==============================================



# Skills Section
with st.container():
    st.markdown('<div id="skills" class="py-8">', unsafe_allow_html=True)
    st.title("Skills Heatmap")
    df_skills = pd.DataFrame(skills_data)
    fig = px.density_heatmap(
        df_skills, x="Category", y="Skill", z="Proficiency", 
        text_auto=True, color_continuous_scale=["#003087", "#FFC107"]
    )
    fig.update_traces(hovertemplate="%{y}: %{z}% proficiency<br>%{customdata}", customdata=df_skills["Details"])
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('<p class="text-center text-gray-600 mt-4">Click skills for details on projects and tools used.</p>', unsafe_allow_html=True)
    st.markdown('</div><hr>', unsafe_allow_html=True)

#===========================================================

# Sample skill data
import streamlit as st
import plotly.graph_objects as go

# Skill Data
skills = {
    "Python": 90,
    "JavaScript": 85,
    "React": 80,
    "Tailwind": 75,
    "Machine Learning": 70,
    "SQL": 65
}
labels = list(skills.keys())
values = list(skills.values())
values += values[:1]
labels += labels[:1]

# Radar Chart
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=values,
    theta=labels,
    fill='toself',
    name='Your Skills',
    line_color='rgba(0,123,255,1)',
    fillcolor='rgba(0,123,255,0.3)',
    hoverinfo='r+theta'
))

# Layout Styling
fig.update_layout(
    polar=dict(
        bgcolor='white',
        radialaxis=dict(
            visible=True,
            range=[0, 100],
            gridcolor='lightgray',
            tickfont=dict(size=12, color='gray')
        ),
        angularaxis=dict(
            tickfont=dict(size=13, color='black')
        )
    ),
    showlegend=False,
    margin=dict(t=30, b=30)
)

st.title("🧠 Skill Radar Chart")
st.plotly_chart(fig, use_container_width=True)



#=========================================================



# Projects Section
with st.container():
    st.markdown('<div id="projects" class="py-8">', unsafe_allow_html=True)
    st.title("Project Impact")
    df_projects = pd.DataFrame(project_data)
    col1, col2 = st.columns([1, 1], gap="medium")
    with col1:
        fig_bar = px.bar(df_projects, x="Project", y="Metric", color="Project", 
                         title="Key Metrics", color_discrete_sequence=["#003087", "#FFC107", "#1E88E5"])
        st.plotly_chart(fig_bar, use_container_width=True)
    with col2:
        fig_line = px.line(df_projects, x="Year", y="Metric", color="Project", 
                           title="Timeline of Impact", markers=True)
        st.plotly_chart(fig_line, use_container_width=True)
    st.markdown("""
    <ul class="list-disc pl-6 text-gray-700 mt-4">
        <li><strong>Agile Adoption</strong>: Boosted efficiency by 40% using JIRA.</li>
        <li><strong>Pipeline Optimization</strong>: Cut runtime by 5.5 hours with Snowflake.</li>
        <li><strong>Qlik-to-Salesforce</strong>: Transitioned 100+ reports seamlessly.</li>
    </ul>
    """, unsafe_allow_html=True)
    st.subheader("Recent GitHub Activity")
    with st.spinner("Fetching GitHub activity..."):
        github_data = get_github_data("Dajinder")
    if not github_data.empty:
        st.dataframe(
            github_data,
            column_config={"Type": "Event Type", "Repo": "Repository", "Date": "Date"},
            hide_index=True,
            use_container_width=True
        )
        fig_github = px.histogram(github_data, x="Date", color="Type", title="Activity Over Time",
                                 color_discrete_sequence=["#003087", "#FFC107", "#1E88E5"])
        st.plotly_chart(fig_github, use_container_width=True)
    else:
        st.write("No recent activity found.")
    st.markdown('</div><hr>', unsafe_allow_html=True)






# -----------------------------------------------------------------------------------------------------------



# Achievements Section
with st.container():
    st.markdown('<div id="achievements" class="py-8">', unsafe_allow_html=True)
    st.title("Achievements")
    col1, col2 = st.columns([1, 1], gap="medium")
    with col1:
        st.markdown("""
        <div class="bg-white p-4 rounded-lg shadow-lg">
            <h3 class="text-xl font-semibold text-windsor-blue mb-2">ZS Client Delight Award 2022</h3>
            <p class="text-gray-700">Recognized for outstanding client impact in analytics and delivery.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="bg-white p-4 rounded-lg shadow-lg">
            <h3 class="text-xl font-semibold text-windsor-blue mb-2">Published Research</h3>
            <p class="text-gray-700">Paper on ML algorithms for Hindi news classification at ICICC.</p>
        </div>
        """, unsafe_allow_html=True)
        paper_path = "paper.pdf"
        if os.path.exists(paper_path):
            st.download_button("Download Paper", data=open(paper_path, "rb").read(), file_name="paper.pdf", key="paper")
        else:
            st.warning("Please add paper.pdf to the folder.")
    st.markdown('</div><hr>', unsafe_allow_html=True)

# Blog Section (Placeholder)
with st.container():
    st.markdown('<div id="blog" class="py-8">', unsafe_allow_html=True)
    st.title("Blog")
    st.markdown('<p class="text-center text-gray-600">Coming soon! Stay tuned for articles on data engineering and analytics.</p>', unsafe_allow_html=True)
    st.markdown('</div><hr>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <footer class="text-center py-6 bg-windsor-blue text-windsor-gold">
        <div class="flex justify-center gap-4">
            <a href="https://linkedin.com/in/yourprofile" class="hover:text-white transition-colors">LinkedIn</a>
            <a href="https://github.com/Dajinder" class="hover:text-white transition-colors">GitHub</a>
            <a href="mailto:your.email@uwindsor.ca" class="hover:text-white transition-colors">Email</a>
        </div>
    </footer>
""", unsafe_allow_html=True)