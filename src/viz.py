"""
Module for visualizing the career path of an
individual based on their starting state and career choices.
"""
from step_and_return import optimal_career_path_to_df
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

CREATE_NEW_DF = True # Change to false if you want to use the existing CSV file
CSV_PATH = 'career_path.csv'

if CREATE_NEW_DF:
    df_list = []
    # TODO could add more start states or explore different interesting values

    start_states = [((0, 0, 0, 18), 0, 5, 0),
                    ((0, 0, 0, 24), 0, 0, 20),
                    ((0, 0, 0, 30), 0, 10, 0),
                    ((0, 0, 0, 40), 40, 0, 0)]

    for i, (start_state, loe, smug, handy) in enumerate(start_states):
        df = optimal_career_path_to_df(start_state, loe, smug, handy)
        df['start_state'] = i
        df_list.append(df)

    df = pd.concat(df_list)
    df.to_csv(CSV_PATH, index=False)
else:
    df = pd.read_csv(CSV_PATH)

# Add a small constant value to the salary to ensure visibility in the plot
df['Adjusted Salary'] = df['Salary'] + 10000  # Adds a minimum size to each bubble

fig = px.scatter(
    df,
    x='Years of Experience',
    y='Years of Education',
    size='Adjusted Salary',
    animation_frame='Age',
    color='Total Savings',
    hover_data={
        'Adjusted Salary': False,  # Do not show Adjusted Salary
        'Salary': True,  # Show actual Salary
        'Total Savings': True,  # Confirming to show Total Savings
        'Years of Education': True,  # Show Years of Education
        'Years of Experience': True,  # Show Years of Experience
        'Age': True  # Show Age
    },
    size_max=60,
    title='Career Progression: Education vs Experience vs Savings',
    labels={
        'Years of Education': 'Years of Education',
        'Years of Experience': 'Years of Work Experience',
        'Total Savings': 'Total Savings ($)',
        'Age': 'Age',
        'start_state': 'Starting State ID',
    },
    range_x=[-2, 50],  # Set the range for the X-axis
    range_y=[-2, 10],  # Set the range for the Y-axis
    color_continuous_scale='RdYlGn'  # Red to Green color scale
)

fig.update_layout(showlegend=True)
fig.show()