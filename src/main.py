import streamlit as st
import pandas as pd
from education_model import optimize_education
from career_model import recommend_career
# from utils import load_data # Removed as we're not using CSV files for data loading anymore
# from optimization import optimize_comprehensive_plan # Assuming this is now handled differently as per instructions
import os
print(os.getcwd())

# Function to save user input to CSV
def save_input_to_csv(data, filename):
    """
    Saves user input data to a CSV file.

    This function takes a dictionary of user input data and a filename, converts the data into a pandas DataFrame,
    and then saves it to a CSV file within the 'data' directory. If the directory does not exist, it will be created.

    Parameters:
    - data (dict): A dictionary containing the user input data to be saved.
    - filename (str): The name of the file (without extension) where the data will be saved.

    Returns:
    None
    """
    df = pd.DataFrame([data])
    # Convert DataFrame to CSV for download instead of saving to a directory
    csv = df.to_csv(index=False)
    # Streamlit download button to allow users to save the file locally
    st.download_button(
        label="Download Your Input Data as CSV",
        data=csv,
        file_name=f"{filename}.csv",
        mime="text/csv",
    )

def main():
    def collect_user_preferences():
        """
        Collects user preferences related to education and career planning.

        This function prompts the user for input on various aspects of their education and career planning,
        including current age, current stage, years in current stage, plans for undergraduate and graduate degrees,
        field of study, anticipated duration of degrees, career preferences, desired retirement age, and vacation frequency.
        The collected information is then stored in a dictionary and returned.

        Returns:
        - dict: A dictionary containing the user's education and career preferences.
        """
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
        """
        Processes user preferences and displays recommended education path and career.

        This function takes the user's preferences, utilizes external models to optimize the education path and recommend
        a career based on those preferences, and then displays the recommendations to the user.

        Parameters:
        - preferences (dict): A dictionary containing the user's education and career preferences.

        Returns:
        None
        """
        # Assuming in-memory data or fetched data for optimization
        education_data = {...}
        career_data = {...}

        # Optimize based on user inputs
        optimized_education_path = optimize_education(preferences, education_data)
        recommended_career = recommend_career(preferences, career_data)

        # Prepare results for CSV export
        results = {
            "Optimized Education Path": optimized_education_path,
            "Recommended Career": recommended_career,
        }
        df_results = pd.DataFrame([results])

        # Convert DataFrame to CSV for download
        csv = df_results.to_csv(index=False)

        # Streamlit download button for results
        st.download_button(
            label="Download Your Optimization Results as CSV",
            data=csv,
            file_name="optimization_results.csv",
            mime="text/csv",
        )
        
        if optimized_education_path and recommended_career:
            st.write("Optimal Life Plan based on your inputs:")
            st.write(f"Optimized Education Path: {optimized_education_path}")
            st.write(f"Recommended Career Path: {recommended_career}")
        else:
            st.write("No optimal plan found based on the inputs.")
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

    if st.button('Generate Optimal Plan'):
        preferences = collect_user_preferences()
        display_recommendations(preferences)

if __name__ == "__main__":
    main()
