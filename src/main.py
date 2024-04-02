import streamlit as st
import pandas as pd
from education_model import optimize_education
from career_model import recommend_career
from utils import load_data

# Function to save user input to CSV
def save_input_to_csv(data, filename):
    df = pd.DataFrame([data])
    df.to_csv(f'data/{filename}.csv', index=False)

def main():
    st.title("EduDynamic Planning")

    # Collecting basic user information
    st.header("Basic Information")
    current_age = st.number_input("Current Age", min_value=16)
    current_stage = st.selectbox("Current Stage", ["High School", "Undergraduate", "Graduate", "Working", "None"])
    years_in_current_stage = st.number_input("Years in Current Stage", min_value=0)

    # Collecting detailed preferences
    st.header("Education and Career Preferences")
    # Example for undergraduate degree
    undergrad_degree = st.checkbox("Plan to pursue an undergraduate degree?")
    undergrad_field = st.text_input("Field of study for undergraduate degree") if undergrad_degree else None
    undergrad_duration = st.number_input("Anticipated duration for undergraduate degree (years)", min_value=1, max_value=10) if undergrad_degree else None
    # Add similar inputs for graduate degree, career preferences, retirement, etc.

    # Collecting lifestyle and financial stability preferences
    st.header("Lifestyle and Financial Preferences")
    retirement_age = st.number_input("Desired retirement age", min_value=current_age)
    vacation_frequency = st.selectbox("Vacation frequency per year", ["None", "1-2 times", "3-5 times", "More than 5 times"])
    # Add more preferences as needed

    # Process and display recommendations based on inputs
    # This part remains largely unchanged, but you may need to adjust the models to consider the new inputs

if __name__ == "__main__":
    main()
