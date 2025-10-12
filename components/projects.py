import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data import get_project_data
from utils.api import get_github_data

def render():
    """Render the projects section"""
    
    with st.container():
        st.markdown('<div id="projects" class="py-8">', unsafe_allow_html=True)
        st.title("🚧 Project Impact & GitHub Activity")
        
        df_projects = pd.DataFrame(get_project_data())
        col1, col2 = st.columns([1, 1], gap="medium")
        
        with col1:
            st.markdown("### 📊 Key Metrics")
            fig_bar = px.bar(
                df_projects, x="Project", y="Metric", color="Project", 
                color_discrete_sequence=["#003087", "#FFC107", "#1E88E5"]
            )
            st.plotly_chart(fig_bar, use_container_width=True)
        
        with col2:
            st.markdown("### ⏳ Timeline of Impact")
            fig_line = px.line(
                df_projects, x="Year", y="Metric", color="Project", 
                markers=True, color_discrete_sequence=["#1E88E5", "#FFC107", "#003087"]
            )
            st.plotly_chart(fig_line, use_container_width=True)
        
        st.markdown("""
        <div class="text-gray-700 mt-4">
            <ul class="list-disc pl-6">
                <li><strong>Agile Adoption</strong>: Boosted efficiency by 40% using JIRA.</li>
                <li><strong>Pipeline Optimization</strong>: Cut runtime by 5.5 hours with Snowflake.</li>
                <li><strong>Qlik-to-Salesforce</strong>: Transitioned 100+ reports seamlessly.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        st.subheader("🔍 Recent GitHub Repositories")
        with st.spinner("Fetching latest GitHub repos..."):
            github_data = get_github_data("Dajinder")
        
        if not github_data.empty:
            for _, row in github_data.iterrows():
                repo_name = row["Repo"].split("/")[1] if "/" in row["Repo"] else row["Repo"]
                st.markdown(f"""
                <div style='border:1px solid #E5E7EB; padding:12px; border-radius:12px; margin:8px 0;'>
                    <strong style='font-size:16px; color:#1E3A8A;'>{repo_name}</strong><br>
                    <small>📦 Repo: <a href='https://github.com/{row['Repo']}' target='_blank'>{row['Repo']}</a></small><br>
                    <small>🗓️ Event: {row['Type']} — {row['Date']}</small>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No recent GitHub activity found.")
        
        st.markdown('</div><hr>', unsafe_allow_html=True)
