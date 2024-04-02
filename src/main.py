import streamlit as st
import pandas as pd
import plotly.express as px
from education_model import optimize_education
from career_model import recommend_career
import os
print(os.getcwd())

def save_input_to_csv(data, filename):
    df = pd.DataFrame([data])
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download Your Input Data as CSV",
        data=csv,
        file_name=f"{filename}.csv",
        mime="text/csv",
    )

def main():
    def collect_user_preferences():
        preferences = {
            "current_age": current_age,
            "current_stage": current_stage,
            "years_in_current_stage": years_in_current_stage,
            "undergrad_degree": undergrad_degree,
            "undergrad_field": undergrad_field,
            "undergrad_duration": undergrad_duration,
            "retirement_age": retirement_age,
            "vacation_frequency": vacation_frequency
        }
        return preferences

    def display_recommendations(preferences):
        education_data = {
            "paths": [
                {"name": "Computer Science", "duration": 4, "cost": 40000, "benefit": 100000},
                {"name": "Business Administration", "duration": 4, "cost": 35000, "benefit": 90000},
            ]
        }
        career_data = {
            "careers": [
                {"name": "Software Engineer", "industry": "Technology", "salary": 100000, "satisfaction": 80},
                {"name": "Project Manager", "industry": "Business", "salary": 85000, "satisfaction": 70},
            ]
        }

        optimized_education_path = optimize_education(preferences, education_data)
        recommended_career = recommend_career(preferences, career_data)

        # Generate the timeline data
        timeline_data = {
            "Start Age": [step['start_age'] for step in optimized_education_path],
            "End Age": [step['end_age'] for step in optimized_education_path],
            "Description": [step['description'] for step in optimized_education_path]
        }

        # Create a DataFrame from the timeline data
        df_timeline = pd.DataFrame(timeline_data)

        # Create a Gantt chart (timeline) using Plotly
        fig = px.timeline(df_timeline, x_start="Start Age", x_end="End Age", y="Description", labels={"Description": "Life Stage"})
        fig.update_yaxes(autorange="reversed")  # Optional: reverse the Y-axis to have the earliest stage at the top

        # Display the Plotly figure in Streamlit
        st.plotly_chart(fig)
        
    st.title("EduDynamic Planning")

    st.header("Basic Information")
    current_age = st.number_input("Current Age", min_value=16)
    current_stage = st.selectbox("Current Stage", ["High School", "Undergraduate", "Graduate", "Working", "None"])
    years_in_current_stage = st.number_input("Years in Current Stage", min_value=0)

    st.header("Education and Career Preferences")
    undergrad_degree = st.checkbox("Plan to pursue an undergraduate degree?")
    undergrad_field_options = ["Computer Science", "Business Administration", "Engineering", "Biology", "Psychology", "English Literature", "Other"]
    undergrad_field = st.selectbox("Field of study for undergraduate degree", options=undergrad_field_options) if undergrad_degree else None
    undergrad_duration = st.number_input("Anticipated duration for undergraduate degree (years)", min_value=1, max_value=10) if undergrad_degree else None
    # Add similar inputs for graduate degree, career preferences, retirement, etc.

    # Collecting lifestyle and financial stability preferences
    st.header("Lifestyle and Financial Preferences")
    retirement_age = st.number_input("Desired retirement age", min_value=current_age)
    vacation_frequency = st.selectbox("Vacation frequency per year", ["None", "1-2 times", "3-5 times", "More than 5 times"])
    # Add more preferences as needed

    if st.button('Generate Optimal Plan'):
        preferences = collect_user_preferences()
        display_recommendations(preferences)

if __name__ == "__main__":
    main()
