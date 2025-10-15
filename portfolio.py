import streamlit as st
# from components import navbar, home, timeline, skills, projects, achievements, blog
from components import navbar, home, timeline, skills, projects, achievements, blog

# Import theme configuration
from utils.theme import set_page_config, apply_custom_styling, init_session_state, setup_responsive_layout

# Initialize theme and layout
set_page_config()
apply_custom_styling()
init_session_state()
setup_responsive_layout()

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
    <footer class="text-center py-6 bg-windsor-blue text-windsor-gold" style="width: 100%; text-align: center;">
        <div style="display: flex; justify-content: center; align-items: center; gap: 2rem; margin: 0 auto; max-width: 600px;">
            <a href="https://linkedin.com/in/yourprofile" class="hover:text-white transition-colors" style="text-decoration: none; padding: 0.5rem;">LinkedIn</a>
            <a href="https://github.com/Dajinder" class="hover:text-white transition-colors" style="text-decoration: none; padding: 0.5rem;">GitHub</a>
            <a href="mailto:your.email@uwindsor.ca" class="hover:text-white transition-colors" style="text-decoration: none; padding: 0.5rem;">Email</a>
        </div>
    </footer>
""", unsafe_allow_html=True)