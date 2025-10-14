import streamlit as st
# from components import navbar, home, timeline, skills, projects, achievements, blog
from .components import navbar, home, timeline, skills, projects, achievements, blog

# Set page config
st.set_page_config(
    page_title="Dajinder | Data-Driven Portfolio", 
    layout="wide", 
    page_icon="📊"
)

# Include base styles
st.markdown("""
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        html { scroll-behavior: smooth; }
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
        .stTitle, h1 {
            color: #003087 !important;
        }
        hr {
            border-top: 1px solid #003087;
            margin: 1rem 0;
        }
    </style>
""", unsafe_allow_html=True)

# Configure Tailwind
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

# Initialize session states - timeline specific
if "last_timeline_click" not in st.session_state:
    st.session_state.last_timeline_click = None

# Initialize session states - skills specific
if "selected_skill_category" not in st.session_state:
    st.session_state.selected_skill_category = "Programming"

# Render navbar
navbar.render()

# Render sections
home.render()
timeline.render()
skills.render_skills_radar()
projects.render()
achievements.render()
blog.render()

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