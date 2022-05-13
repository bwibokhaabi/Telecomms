import streamlit as st
import pandas as pd
import sys
sys.path.insert(0, '../scripts')

from results_pickler import ResultPickler

def app():

    # Load Saved Results Data
    results = ResultPickler()
    results.load_data(file_name='./data/engagement_results.pickle')

    st.title("User Engagement analysis")

    st.header("Top 10 Users")
    st.subheader("Based on: Session Count")
    st.dataframe(results.data['session_frequency'])

    st.subheader("Based on: Total Duration (hr)")
    st.dataframe(results.data['session_duration'])

    st.subheader("Based on: Total Data Traffic (MegaBytes)")
    st.dataframe(results.data['total_session_b'])

    st.header("Top 10 Users Engaged Per Each Application")
    st.subheader("Social Media App")
    st.dataframe(results.data['social_media_traffic'])

    st.subheader("Google")
    st.dataframe(results.data['google_traffic'])
    
    st.subheader("Email")
    st.dataframe(results.data['email_traffic'])

    st.subheader("Youtube")
    st.dataframe(results.data['youtube_traffic'])

    st.subheader("Netflix")
    st.dataframe(results.data['netflix_traffic'])

    st.subheader("Gaming")
    st.dataframe(results.data['gaming_traffic'])

    st.subheader("Other Apps")
    st.dataframe(results.data['other_traffic'])

    st.header("Top 3 Most Used Applications")
    st.dataframe(results.data['most_used_apps'])

    st.header("Users Clustering")
    st.image('./data/engagement_cluster.png')