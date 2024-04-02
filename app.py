import streamlit as st
import pandas as pd

# Function to save user input to CSV
def save_input_to_csv(data, filename):
    df = pd.DataFrame([data])
    df.to_csv(f'data/{filename}.csv', index=False)

# Streamlit app
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

    # Button to save inputs to CSV
    if st.button("Save Preferences"):
        education_preferences = {'max_cost': max_cost, 'field': preferred_field}
        career_preferences = {'min_salary': min_salary, 'industry': preferred_industry}

        # Save to CSV files
        save_input_to_csv(education_preferences, 'education_data')
        save_input_to_csv(career_preferences, 'career_data')

        st.success("Preferences saved!")

if __name__ == "__main__":
    main()