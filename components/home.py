import streamlit as st
import os
import base64

def render():
    """Render the home section with interactive elements"""
    # Add custom CSS for animations and styling
    st.markdown("""
    <style>
    .profile-container {
        animation: fadeIn 1s ease-in;
    }
    
    .profile-header {
        background: linear-gradient(135deg, #2C2A4A 0%, #4A4875 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin-bottom: 2rem;
    }
    
    .highlight-text {
        color: #FFD700;
        font-weight: bold;
    }
    
    .profile-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        transition: transform 0.3s ease;
    }
    
    .profile-card:hover {
        transform: translateY(-5px);
    }
    
    .download-resume-btn {
        display: inline-flex;
        align-items: center;
        padding: 0.75rem 1.5rem;
        background: linear-gradient(135deg, #2C2A4A 0%, #4A4875 100%);
        color: white;
        border-radius: 25px;
        text-decoration: none;
        font-weight: bold;
        transition: all 0.3s ease;
        margin-top: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .download-resume-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div id="home" class="profile-container">', unsafe_allow_html=True)
        
        # Profile Header
        st.markdown("""
        <div class="profile-header">
            <h1>Hi, I'm <span class="highlight-text">Dajinder Singh!</span> 👋</h1>
            <p style="font-size: 1.2rem; margin-top: 1rem;">
                A passionate <span class="highlight-text">Data</span> and <span class="highlight-text">AI</span> enthusiast
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1], gap="medium")
        
        with col1:
            # Profile Image with caption
            st.image("utils/docs/Profile_Image_cp.png", use_container_width=True)
        
        with col2:
            # About Me Card
            st.markdown("""
            <div class="profile-card">
                <h3 style="color: #2C2A4A; margin-bottom: 1rem;">About Me</h3>
                <p style="line-height: 1.6;">
                    Master's student in Applied Computing at University of Windsor with 4 years at ZS Associates. 
                    Experienced in business analysis, data engineering, and analytics. Expert in:
                </p>
                <ul style="list-style-type: none; padding-left: 0; margin-top: 1rem;">
                    <li>🐍 Python Development</li>
                    <li>❄️ Snowflake</li>
                    <li>📊 Data Analytics</li>
                    <li>🎯 Agile Project Management</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            # Resume Download Section
            resume_path = "utils/docs/Dajinder_Singh_Resume.pdf"
            if os.path.exists(resume_path):
                with open(resume_path, "rb") as pdf_file:
                    pdf_data = pdf_file.read()
                
                # Styled download button
                st.markdown("""
                <div class="profile-card" style="text-align: center;">
                    <h4 style="color: #2C2A4A; margin-bottom: 1rem;">Want to know more?</h4>
                """, unsafe_allow_html=True)
                
                st.download_button(
                    label="📄 Download Resume",
                    data=pdf_data,
                    file_name="Dajinder_Singh_Resume.pdf",
                    mime="application/pdf",
                    key="resume",
                    help="Click to download my latest resume",
                    use_container_width=True
                )
                
                st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.warning("Resume file not found. Please check the file path.")
        
        # Quick Stats Section
        # st.markdown("""
        # <div style="display: flex; justify-content: space-around; margin-top: 2rem;">
        #     <div class="profile-card" style="flex: 1; margin: 0 0.5rem; text-align: center;">
        #         <h3 style="color: #2C2A4A;">4+</h3>
        #         <p>Years Experience</p>
        #     </div>
        #     <div class="profile-card" style="flex: 1; margin: 0 0.5rem; text-align: center;">
        #         <h3 style="color: #2C2A4A;">10+</h3>
        #         <p>Projects Completed</p>
        #     </div>
        #     <div class="profile-card" style="flex: 1; margin: 0 0.5rem; text-align: center;">
        #         <h3 style="color: #2C2A4A;">3+</h3>
        #         <p>Awards Won</p>
        #     </div>
        # </div>
        # """, unsafe_allow_html=True)
        
        # st.markdown('</div><hr>', unsafe_allow_html=True)
        
        # st.markdown('</div><hr>', unsafe_allow_html=True)
