def get_skills_data():
    """Return skills data"""
    return {
        "Category": ["Data Analysis", "Data Analysis", "Tools", "Tools", "Tools", "Tools", "Database", "Database", "Programming", "Programming", "Project Management"],
        "Skill": ["Excel", "Qlik Sense", "Snowflake", "Salesforce", "Streamlit", "JIRA", "Snowflake", "MySQL", "Python", "Java", "JIRA"],
        "Proficiency": [90, 85, 88, 80, 75, 90, 88, 80, 92, 85, 90],
        "Details": [
            "Advanced analytics and pivots", "Built client reports", "Optimized pipelines",
            "Managed Qlik-to-SF transition", "Built portfolio apps", "Agile project tracking",
            "Pipeline design", "Query optimization", "Data pipelines & ML", "CLI apps", "Sprint planning"
        ]
    }

def get_project_data():
    """Return project data"""
    return {
        "Project": ["Agile Adoption", "Pipeline Optimization", "Qlik-to-Salesforce"],
        "Impact": ["40% efficiency increase", "Reduced runtime from 8 to 2.5 hours", "Smooth transition for 100+ reports"],
        "Year": [2024, 2023, 2023],
        "Metric": [40, 5.5, 100]
    }