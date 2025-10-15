import streamlit as st

def set_page_config():
    """Configure the page settings and theme"""
    st.set_page_config(
        page_title="Dajinder Singh - Portfolio",
        page_icon="👨‍💻",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def apply_custom_styling():
    """Apply custom CSS styling for a professional look"""
    st.markdown("""
        <style>
        /* Main theme colors */
        :root {
            --primary-color: #2196F3;
            --secondary-color: #4CAF50;
            --background-color: #FAFAFA;
            --text-color: #333333;
            --accent-color: #FF5722;
        }
        
        /* Typography */
        html, body, [class*="css"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        h1, h2, h3 {
            color: var(--text-color);
            font-weight: 600;
        }
        
        /* Responsive containers */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        @media (max-width: 768px) {
            .container {
                padding: 1rem;
            }
        }
        
        /* Card styling */
        .stcard {
            background-color: white;
            border-radius: 10px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            transition: transform 0.2s ease;
        }
        
        .stcard:hover {
            transform: translateY(-5px);
        }
        
        /* Timeline customization */
        .timeline-component {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #f8f9fa;
            padding: 2rem 1rem;
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary-color);
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            border: none;
            transition: all 0.2s ease;
        }
        
        .stButton>button:hover {
            background-color: var(--secondary-color);
            transform: translateY(-2px);
        }
        
        /* Skills section */
        .skill-tag {
            display: inline-block;
            background-color: #e9ecef;
            padding: 0.3rem 0.8rem;
            border-radius: 15px;
            margin: 0.2rem;
            font-size: 0.9rem;
            transition: background-color 0.2s ease;
        }
        
        .skill-tag:hover {
            background-color: var(--primary-color);
            color: white;
        }
        
        /* Responsive images */
        img {
            max-width: 100%;
            height: auto;
            border-radius: 5px;
        }
        
        /* Loading animation */
        .loading {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100px;
        }
        
        /* Section spacing */
        .section {
            margin: 2rem 0;
            padding: 2rem 0;
            border-bottom: 1px solid #eee;
        }
        
        /* Responsive grid */
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1rem;
        }
        
        /* Animation classes */
        .fade-in {
            animation: fadeIn 0.5s ease-in;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
        }
        
        ::-webkit-scrollbar-thumb {
            background: var(--primary-color);
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: var(--secondary-color);
        }
        </style>
    """, unsafe_allow_html=True)

def init_session_state():
    """Initialize session state variables"""
    if 'theme' not in st.session_state:
        st.session_state.theme = 'light'
    if 'animation_enabled' not in st.session_state:
        st.session_state.animation_enabled = True
    if 'is_mobile' not in st.session_state:
        st.session_state.is_mobile = False

def setup_responsive_layout():
    """Set up responsive layout based on screen size"""
    # Detect mobile devices (this is a basic implementation)
    st.session_state.is_mobile = False  # You can implement proper detection if needed
    
    if st.session_state.is_mobile:
        # Mobile-specific settings
        st.markdown("""
            <style>
            .container { padding: 0.5rem; }
            .grid { grid-template-columns: 1fr; }
            </style>
        """, unsafe_allow_html=True)