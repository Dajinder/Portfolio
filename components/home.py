import streamlit as st
import os
import base64

def render():
    """Render the home section"""
    with st.container():
        st.markdown('<div id="home" class="py-8">', unsafe_allow_html=True)
        st.title("Hi, I'm Dajinder!")
        st.markdown("""
        Master's student in Applied Computing at University of Windsor with 4 years at ZS Associates in business analysis, 
        data engineering, and analytics. Expert in Python, Snowflake, and JIRA, driving efficiency and insights for global clients.
        """)
        
        col1, col2 = st.columns([1, 1], gap="medium")
        with col1:
            st.image("C:/Users/singh/Downloads/Profile_Image_cp.png", caption="Your Photo", width=500)
        with col2:
            # st.markdown("""
            # <div class="bg-white p-4 rounded-lg shadow-lg">
            #     <h3 class="text-xl font-semibold text-windsor-blue mb-2">About Me</h3>
            #     <p class="text-gray-700">Published ML research, won ZS Client Delight Award 2022. Passionate about data pipelines, Agile, and impactful solutions.</p>
            # </div>
            # """, unsafe_allow_html=True)
            
            resume_path = "C:/UWindsor/Co-op/ZS/Dajinder_Singh_Resume.pdf"
            if os.path.exists(resume_path):
                
                # Read and encode the PDF for preview
                with open(resume_path, "rb") as pdf_file:
                    pdf_data = pdf_file.read()
                    base64_pdf = base64.b64encode(pdf_data).decode('utf-8')
                
                # # Display PDF preview in an iframe
                # st.markdown("### Resume Preview")
                # pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="400px" type="application/pdf"></iframe>'
                # st.markdown(pdf_display, unsafe_allow_html=True)
                
                # Keep the existing download button
                st.download_button(
                    "Download Resume", 
                    data=pdf_data, 
                    file_name="Dajinder_Singh_Resume.pdf", 
                    key="resume"
                )
                st.pdf(resume_path)
            else:
                st.warning("Please add resume.pdf to the folder.")
        
        st.markdown('</div><hr>', unsafe_allow_html=True)
