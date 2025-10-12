import streamlit as st
import pandas as pd
import requests
from datetime import datetime

@st.cache_data(ttl=3600)
def get_github_data(username):
    """Fetch GitHub activity data"""
    try:
        events_url = f"https://api.github.com/users/{username}/events/public"
        response = requests.get(events_url, timeout=5)
        if response.status_code != 200:
            return pd.DataFrame()
        
        events = response.json()
        recent_repos = []
        for e in events[:5]:
            if "repo" in e:
                recent_repos.append({
                    "Repo": e["repo"]["name"],
                    "Type": e["type"],
                    "Date": e["created_at"][:10]
                })
        return pd.DataFrame(recent_repos)
    except:
        return pd.DataFrame()