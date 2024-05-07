from step_and_return import bellman, possible_states, terminal_state, reward, available_actions, optimal_career_path_to_df
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df= optimal_career_path_to_df((0, 0, 0, 18))

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
        'Age': 'Age'
    },
    range_x=[-2, 50],  # Set the range for the X-axis
    range_y=[-2, 10],  # Set the range for the Y-axis
    color_continuous_scale='RdYlGn'  # Red to Green color scale
)

fig.update_layout(showlegend=True)
fig.show()