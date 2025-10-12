import streamlit as st

def render():
    """Render the navigation bar with working mobile menu"""
    
    st.markdown("""
    <style>
    .navbar {
        background-color: #2C2A4A;
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
    
    .nav-heading {
        color: white;
        font-weight: bold;
        font-size: 1.25rem;
    }
    
    .nav-links {
        display: flex;
        gap: 1.5rem;
    }
    
    .nav-links a {
        color: white;
        text-decoration: none;
        font-weight: bold;
        padding: 5px;
    }
    
    .nav-links a:hover {
        color: #FFD700;
    }
    
    .mobile-menu-wrapper {
        display: none;
        position: relative;
    }
    
    .mobile-menu-btn {
        font-size: 1.5rem;
        color: white;
        cursor: pointer;
        background: none;
        border: none;
        outline: none;
        padding: 0.5rem;
    }
    
    .mobile-dropdown {
        position: absolute;
        top: 100%;
        right: 0;
        background-color: #2C2A4A;
        min-width: 200px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        border-radius: 0.5rem;
        margin-top: 0.5rem;
        z-index: 100;
        opacity: 0;
        visibility: hidden;
        transform: translateY(-10px);
        transition: all 0.3s ease;
    }
    
    .mobile-dropdown.show {
        opacity: 1;
        visibility: visible;
        transform: translateY(0);
    }
    
    .mobile-dropdown a {
        display: block;
        color: white;
        text-decoration: none;
        font-weight: bold;
        padding: 0.75rem 1rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .mobile-dropdown a:hover {
        background-color: rgba(255, 215, 0, 0.2);
        color: #FFD700;
    }
    
    .mobile-dropdown a:last-child {
        border-bottom: none;
    }
    
    @media (max-width: 768px) {
        .nav-links {
            display: none;
        }
        .mobile-menu-wrapper {
            display: block;
        }
    }
    </style>
    
    <div class="navbar">
        <div class="nav-heading">Dajinder</div>
        <div class="nav-links">
            <a href="#home">Home</a>
            <a href="#experience">Career Timeline</a>
            <a href="#skills">Skills</a>
            <a href="#projects">Projects</a>
            <a href="#achievements">Achievements</a>
            <a href="#blog">Blog</a>
        </div>
        <div class="mobile-menu-wrapper">
            <button class="mobile-menu-btn" id="mobileMenuBtn">☰</button>
            <div class="mobile-dropdown" id="mobileDropdown">
                <a href="#home">🏠 Home</a>
                <a href="#experience">💼 Career Timeline</a>
                <a href="#skills">🎯 Skills</a>
                <a href="#projects">🚀 Projects</a>
                <a href="#achievements">🏆 Achievements</a>
                <a href="#blog">📝 Blog</a>
            </div>
        </div>
    </div>
    
    <script>
    (function() {
        // Wait for DOM to be ready
        setTimeout(function() {
            const btn = document.getElementById('mobileMenuBtn');
            const dropdown = document.getElementById('mobileDropdown');
            
            if (btn && dropdown) {
                // Toggle dropdown
                btn.addEventListener('click', function(e) {
                    e.stopPropagation();
                    dropdown.classList.toggle('show');
                });
                
                // Close when clicking a link
                const links = dropdown.querySelectorAll('a');
                links.forEach(function(link) {
                    link.addEventListener('click', function() {
                        dropdown.classList.remove('show');
                    });
                });
                
                // Close when clicking outside
                document.addEventListener('click', function(e) {
                    if (!btn.contains(e.target) && !dropdown.contains(e.target)) {
                        dropdown.classList.remove('show');
                    }
                });
            }
        }, 100);
    })();
    </script>
    """, unsafe_allow_html=True)
    
    # Add spacing
    st.markdown('<div style="height: 80px;"></div>', unsafe_allow_html=True)
