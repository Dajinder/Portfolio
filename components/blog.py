import streamlit as st

def render():
    """Render the blog section"""
    
    with st.container():
        st.markdown('<div id="blog" class="py-8">', unsafe_allow_html=True)
        st.title("Blog")
        st.markdown(
            '<p class="text-center text-gray-600">Coming soon! Stay tuned for articles on Data Engineering, Analytics and AI.</p>', 
            unsafe_allow_html=True
        )
        st.markdown('</div><hr>', unsafe_allow_html=True)