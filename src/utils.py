import pandas as pd

def load_data():
    """
    Loads education and career data from CSV files.

    This function reads data from 'education_data.csv' and 'career_data.csv' files located in the 'data' directory.
    It returns two pandas DataFrames containing the loaded data for further processing.

    Returns:
    - education_data (DataFrame): A pandas DataFrame containing the education data.
    - career_data (DataFrame): A pandas DataFrame containing the career data.
    """
    education_data = pd.read_csv('data/education_data.csv')
    career_data = pd.read_csv('data/career_data.csv')
    return education_data, career_data
