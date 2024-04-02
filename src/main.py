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
    st.title("EduDynamic User Input")

    # Collecting user preferences for education model
    st.header("Education Preferences")
    max_cost = st.number_input("Maximum Cost", min_value=0)
    preferred_field = st.text_input("Preferred Field of Study")

    # Collecting user preferences for career model
    st.header("Career Preferences")
    min_salary = st.number_input("Minimum Salary", min_value=0)
    preferred_industry = st.text_input("Preferred Industry")

    # Button to save inputs and process models
    if st.button("Save Preferences and Process"):
        user_preferences = {
            'education': {'max_cost': max_cost, 'field': preferred_field},
            'career': {'min_salary': min_salary, 'industry': preferred_industry}
        }

        # Save to CSV files
        save_input_to_csv(user_preferences['education'], 'education_data')
        save_input_to_csv(user_preferences['career'], 'career_data')

        # Load data
        education_data, career_data = load_data()

        # Process inputs through models
        education_path = optimize_education(user_preferences['education'], education_data)
        career_path = recommend_career(user_preferences['career'], career_data)

        # Display results
        st.write("Recommended Education Path:", education_path)
        st.write("Recommended Career Path:", career_path)

if __name__ == "__main__":
    main()