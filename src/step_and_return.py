import math
import numpy as np
import pandas as pd
import random

def get_salary(state, action):
    """
    Calculate a random salary based on the provided state.

    Args:
        state (tuple): A tuple representing the current state, containing:
            - Years of education (int)
            - Years of experience (int)
    
    Returns:
        int: A random salary based on the state.
    """

    if action == 1:
        return 0
    # Define salary ranges based on education and experience levels
    min_salary = np.array([[24, 30, 40, 55, 85],
                           [45, 60, 70, 80, 100],
                           [70, 85, 95, 105, 125],
                           [85, 95, 115, 135, 150]])
    max_salary = np.array([[27, 38, 50, 85, 150],
                           [60, 70, 100, 120, 200],
                           [85, 100, 110, 125, 225],
                           [95, 120, 135, 160, 300]])
    
    # Determine the range index based on years of education and experience
    if state[0] < 4:
        x = 0
    elif state[0] < 6:
        x = 1
    elif state[0] < 8:
        x = 2
    else:
        x = 3

    if state[1] < 5:
        y = 0
    elif state[1] < 10:
        y = 1
    elif state[1] < 15:
        y = 2
    elif state[1] < 20:
        y = 3
    else:
        y = 4
    
    # Generate a random salary within the determined range
    salary = random.randint(min_salary[x, y], max_salary[x, y]) * 1000
    return salary

def possible_states(state, action):
    """
    Determine the possible next states based on the current state and action.

    Args:
        state (tuple): A tuple representing the current state, containing:
            - Years of education (int)
            - Years of experience (int)
            - Total savings (int)
            - Age (int)
        action (int): The action to be taken, where 0 represents no action and 1 represents advancing education.

    Returns:
        list of tuples: A list containing tuples representing possible next states and their probabilities.
    """
    poss_salary1 = get_salary(state,action)
    poss_salary2 = get_salary(state,action)

    # Define the cost of living
    cost_of_living = 30000

    if action == 1:
        # If action is to advance education, subtract education cost from savings
        total_savings1 = state[2] - 20000 + poss_salary1
        total_savings2 = state[2] - 20000 + poss_salary2

        years_edu = state[0] + 1
        years_exp = state[1]
    else:
        # If no action is taken, add salary to savings
        total_savings1 = state[2] + poss_salary1
        total_savings2 = state[2] + poss_salary2
        years_exp = state[1] + 1
        years_edu = state[0]
    
    # Create possible next states
    state1 = (years_edu, years_exp, total_savings1 - cost_of_living, state[3] + 1)
    state2 = (years_edu, years_exp, total_savings2 - cost_of_living, state[3] + 1)

    # Return possible next states with equal probabilities
    return [(0.5, state1),
            (0.5, state2)]

def reward(state, action):
    """
    Calculate the reward based on the current state and action.

    Args:
        state (tuple): A tuple representing the current state, containing:
            - Years of education (int)
            - Years of experience (int)
            - Total savings (int)
            - Age (int)
        action (int): The action taken, where 0 represents no action and 1 represents advancing education.

    Returns:
        int: The reward, which is the current total savings.
    """
    return state[2]

def available_actions(state):
    """
    Determine the available actions based on the current state.

    Args:
        state (tuple): A tuple representing the current state, containing:
            - Years of education (int)
            - Years of experience (int)
            - Total savings (int)
            - Age (int)

    Returns:
        list: A list containing available actions, where 0 represents no action and 1 represents advancing education.
    """
    # Prevent education past 8 years
    if state[0] == 8:
        return [0]

    return [0, 1]

def terminal_state(state):
    """
    Check if the current state is a terminal state.

    Args:
        state (tuple): A tuple representing the current state, containing:
            - Years of education (int)
            - Years of experience (int)
            - Total savings (int)
            - Age (int)

    Returns:
        tuple: A tuple containing a boolean indicating if the state is terminal and, if so, the terminal return.
    """
    # Terminal state reached at age 65
    if state[3] >= 65:
        return True, (state[2], -1)  # Return savings and a special action value indicating terminal state
    else:
        return False, ()

cache = {}

def bellman(state):
    """
    Apply the Bellman equation to find the optimal action and value for a given state.

    Args:
        state (tuple): A tuple representing the current state, containing:
            - Years of education (int)
            - Years of experience (int)
            - Total savings (int)
            - Age (int)

    Returns:
        tuple: A tuple containing the optimal value and action for the given state.
    """
    is_terminal, term_return = terminal_state(state)
    if is_terminal:
        return term_return
    if state in cache:
        return cache[state]
    best_value = None
    best_action = None
    for action in available_actions(state):
        exp_action_value = 0
        for p_state, next_state in possible_states(state, action):
            # Calculate the expected action value using Bellman equation
            exp_action_value += p_state * (reward(state, action) + bellman(next_state)[0])
        if best_value is None or exp_action_value > best_value:
            best_value = exp_action_value
            best_action = action
    cache[state] = (best_value, best_action)
    return best_value, best_action

# Example of using the Bellman equation to find the optimal action and value for a given state
#print(bellman((0, 0, 0, 18)))
'''
start_state = (0, 0, 0, 18)
state = start_state
state_actions = []
while not terminal_state(state)[0]:
  best_value, best_action = bellman(state)
  state_actions.append((state, best_action))
  states = possible_states(state, best_action)
  state = random.choices([s[1] for s in states],
                          weights=[s[0] for s in states])[0]
print(state_actions)
'''

def optimal_career_path_to_df(start_state):
    """
    Simulate a career path based on a start state using the Bellman equation.

    Args:
        start_state (tuple): Initial state tuple (Years of Education, Years of Experience, Total Savings, Age)

    Returns:
        DataFrame: A pandas DataFrame containing the simulated career path.
    """
    state = start_state
    state_actions = []
    
    while not terminal_state(state)[0]:
        best_value, best_action = bellman(state)
        state_actions.append((state, best_action))
        states = possible_states(state, best_action)
        state = random.choices([s[1] for s in states], weights=[s[0] for s in states])[0]
    
    # Extract data from state_actions to create a DataFrame
    data = {
        'Years of Education': [s[0][0] for s in state_actions],
        'Years of Experience': [s[0][1] for s in state_actions],
        'Total Savings': [s[0][2] for s in state_actions],
        'Age': [s[0][3] for s in state_actions],
        'Salary': [get_salary(s[0], s[1]) for s in state_actions]
    }

    df = pd.DataFrame(data)
    return df

