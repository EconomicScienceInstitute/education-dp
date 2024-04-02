import pandas as pd

def load_data():
    education_data = pd.read_csv('data/education_data.csv')
    career_data = pd.read_csv('data/career_data.csv')
    return education_data, career_data
