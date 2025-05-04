import streamlit as st
import pandas as pd
import plotly.express as px
import requests
from datetime import datetime
from streamlit_timeline import st_timeline
import os

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

# Responsive Navigation Bar with Hamburger Menu

# with st.container():

#     st.markdown('<div class="nav-bar">', unsafe_allow_html=True)
#     cols = st.columns(6)
#     sections = ["Home", "Skills", "Projects", "Timeline", "Achievements", "Blog"]
#     for col, section in zip(cols, sections):
#         with col:
#             # JavaScript for smooth scrolling
#             st.markdown(
#                 f'<a href="#{section.lower()}" class="nav-button" onclick="document.getElementById(\'{section.lower()}\').scrollIntoView({{behavior: \'smooth\'}});">{section}</a>',
#                 unsafe_allow_html=True
#             )
#     st.markdown('</div>', unsafe_allow_html=True)



# with st.container():
#     st.markdown("""
#     <div class="flex items-center justify-between px-4 py-2 bg-windsor-blue text-white sticky top-0 z-50">
#         <div class="text-lg font-bold">Dajinder</div>
#         <button class="md:hidden" onclick="toggleMenu()">
#             <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
#                 stroke="currentColor">
#                 <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
#                     d="M4 6h16M4 12h16M4 18h16" />
#             </svg>
#         </button>
#         <div id="navLinks" class="hidden md:flex space-x-4">
#             <a href="#home" class="hover:text-windsor-gold" onclick="scrollToSection('home')">Home</a>
#             <a href="#skills" class="hover:text-windsor-gold" onclick="scrollToSection('skills')">Skills</a>
#             <a href="#projects" class="hover:text-windsor-gold" onclick="scrollToSection('projects')">Projects</a>
#             <a href="#timeline" class="hover:text-windsor-gold" onclick="scrollToSection('timeline')">Timeline</a>
#             <a href="#achievements" class="hover:text-windsor-gold" onclick="scrollToSection('achievements')">Achievements</a>
#             <a href="#blog" class="hover:text-windsor-gold" onclick="scrollToSection('blog')">Blog</a>
#         </div>
#     </div>
#     <script>
#         function toggleMenu() {
#             var menu = document.getElementById("navLinks");
#             if (menu.classList.contains("hidden")) {
#                 menu.classList.remove("hidden");
#                 menu.classList.add("flex", "flex-col", "space-y-2", "mt-2");
#             } else {
#                 menu.classList.add("hidden");
#                 menu.classList.remove("flex", "flex-col", "space-y-2", "mt-2");
#             }
#         }

#         function scrollToSection(id) {
#             document.getElementById(id).scrollIntoView({ behavior: 'smooth' });
#         }
#     </script>
#     """, unsafe_allow_html=True)


# --- Responsive Navbar using Streamlit toggle ---
# if 'menu_visible' not in st.session_state:
#     st.session_state.menu_visible = False

# def toggle_menu():
#     st.session_state.menu_visible = not st.session_state.menu_visible

# with st.container():
#     st.markdown('<div class="flex items-center justify-between px-4 py-2 bg-windsor-blue text-white sticky top-0 z-50">', unsafe_allow_html=True)
#     col1, col2 = st.columns([8, 1])
#     with col1:
#         st.markdown('<div class="text-lg font-bold">Dajinder</div>', unsafe_allow_html=True)
#     with col2:
#         st.button("☰", on_click=toggle_menu, key="hamburger")

#     if st.session_state.menu_visible:
#         st.markdown("""
#             <div class="flex flex-col space-y-2 mt-2 text-white">
#                 <a href="#home" class="hover:text-windsor-gold">Home</a>
#                 <a href="#skills" class="hover:text-windsor-gold">Skills</a>
#                 <a href="#projects" class="hover:text-windsor-gold">Projects</a>
#                 <a href="#timeline" class="hover:text-windsor-gold">Timeline</a>
#                 <a href="#achievements" class="hover:text-windsor-gold">Achievements</a>
#                 <a href="#blog" class="hover:text-windsor-gold">Blog</a>
#             </div>
#         """, unsafe_allow_html=True)

#     st.markdown("</div>", unsafe_allow_html=True)



# import streamlit as st

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
        <a href="#experience">Professional Experience</a>
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
    <a href="#experience">Professional Experience</a>
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


# Experience Section
with st.container():
    st.markdown('<div id="experience" class="py-8">', unsafe_allow_html=True)
    st.title("Professional Experience")

    # Create Plotly Timeline
    df_experience = pd.DataFrame(experience_data)
    fig = px.timeline(
        df_experience,
        x_start="Start",
        x_end="End",
        y="Task",
        color="Task",
        title="Career Timeline",
        color_discrete_sequence=["#003087", "#FFC107", "#1E88E5", "#FF5722"],
        hover_data={"Company": True, "Start": "|%b %Y", "End": "|%b %Y"}
    )
    # fig.update_yaxes(autorange="reversed")
    fig.update_yaxes()
    fig.update_layout(
        showlegend=False,
        height=300,
        clickmode="event+select",
        xaxis_title="",
        yaxis_title="",
        margin=dict(t=50, b=50)
    )
    fig.update_traces(marker=dict(line=dict(color="#ffffff", width=2)))
    st.plotly_chart(fig, use_container_width=True)

    # Initialize session state
    if "selected_role" not in st.session_state:
        st.session_state.selected_role = "Business Technology Associate Consultant"
    if "show_popup" not in st.session_state:
        st.session_state.show_popup = False

    # Hidden text input to capture clicked role
    clicked_role = st.text_input("Clicked Role", value=st.session_state.selected_role, key="clicked_role", disabled=True)
    if clicked_role and clicked_role != st.session_state.selected_role:
        st.session_state.selected_role = clicked_role
        st.session_state.show_popup = True

    # JavaScript to capture Plotly click and update text input
    st.markdown("""
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        var plot = document.getElementsByClassName('plotly')[0];
        if (plot) {
            plot.on('plotly_click', function(data) {
                var role = data.points[0].y;
                var input = document.querySelector('input[name="clicked_role"]');
                if (input) {
                    input.value = role;
                    input.dispatchEvent(new Event('change', { bubbles: true }));
                }
            });
        }
    });
    </script>
    """, unsafe_allow_html=True)

    # Modal (Popup) for role details
    if st.session_state.show_popup:
        role_data = next((role for role in experience_data if role["Task"] == st.session_state.selected_role), experience_data[0])
        modal_html = """
        <div class="modal-overlay" onclick="closeModal()"></div>
        <div class="fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-white p-6 rounded-lg shadow-lg z-50 w-11/12 max-w-lg">
            <h3 class="text-xl font-semibold text-windsor-blue mb-2">{}</h3>
            <p class="text-lg text-gray-700 mb-4">{} | {} - {}</p>
            <ul class="list-disc pl-6 text-gray-700 mb-4">
        """.format(
            role_data["Task"],
            role_data["Company"],
            datetime.strptime(role_data["Start"], "%Y-%m-%d").strftime("%b %Y"),
            datetime.strptime(role_data["End"], "%Y-%m-%d").strftime("%b %Y")
        )
        for detail in role_data["Details"]:
            modal_html += f'<li>{detail}</li>'
        modal_html += """
            </ul>
            <button class="bg-windsor-gold text-windsor-blue px-4 py-2 rounded hover:bg-yellow-500 transition-colors" onclick="closeModal()">Close</button>
        </div>
        <script>
        function closeModal() {
            var input = document.querySelector('input[name="show_popup"]');
            if (input) {
                input.value = 'False';
                input.dispatchEvent(new Event('change', { bubbles: true }));
            }
        }
        </script>
        """
        st.markdown(modal_html, unsafe_allow_html=True)

        # Hidden input to capture modal close
        show_popup = st.text_input("Show Popup", value=str(st.session_state.show_popup), key="show_popup", disabled=True)
        if show_popup == "False":
            st.session_state.show_popup = False

    st.markdown('</div><hr>', unsafe_allow_html=True)


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

# Timeline Section
with st.container():
    st.markdown('<div id="timeline" class="py-8">', unsafe_allow_html=True)
    st.title("Career Timeline")
    timeline_data = [
        {"id": 1, "content": "B.Tech, GGSIPU", "start": "2017-08-01", "group": "Education"},
        {"id": 2, "content": "Business Analyst Intern, ZS", "start": "2020-12-01", "end": "2021-06-30", "group": "Work"},
        {"id": 3, "content": "Data Engineer, ZS", "start": "2021-07-01", "end": "2023-01-31", "group": "Work"},
        {"id": 4, "content": "Senior Data Engineer, ZS", "start": "2023-01-01", "end": "2023-11-30", "group": "Work"},
        {"id": 5, "content": "Business Analyst, ZS", "start": "2023-12-01", "end": "2025-01-31", "group": "Work"},
        {"id": 6, "content": "MAC, University of Windsor", "start": "2025-01-01", "group": "Education"}
    ]
    st_timeline(timeline_data, groups=[], options={}, height="300px")
    st.markdown('</div><hr>', unsafe_allow_html=True)

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