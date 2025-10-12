import streamlit as st
import os

def render():
    """Render the achievements section"""
    
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
                st.download_button(
                    "Download Paper", 
                    data=open(paper_path, "rb").read(), 
                    file_name="paper.pdf", 
                    key="paper"
                )   
            else:
                st.warning("Please add paper.pdf to the folder.")
        
        st.markdown('</div><hr>', unsafe_allow_html=True)