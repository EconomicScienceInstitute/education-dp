import math
import numpy as np
import pandas as pd
import random

def get_salary(state, action):
    """
    Calculate a random salary based on the provided state.

    Args:
        state (tuple): A tuple representing the current state, containing:
            - Years of education (int) idx: 0
            - Years of experience (int) idx: 1
            - Savings (int, rounded to the nearest thousand) idx: 2
            - Age (int) idx: 3
    
    Returns:
        int: A random salary based on the state.
    """
    # TODO could modify the get_salary function to return a salary based on the state
    # wouldn't that require us to add salary to the state? 
    if action == 1: #go to school
        return 0
    # Define salary ranges based on education and experience levels
    min_salary = np.array([[30, 36, 48, 60, 90],
                           [45, 60, 70, 80, 100],
                           [70, 85, 95, 105, 125],
                           [70, 85, 95, 105, 125]])
    max_salary = np.array([[35, 41, 55, 90, 150],
                           [60, 70, 100, 120, 200],
                           [85, 100, 110, 125, 225],
                           [80, 95, 105, 120, 210]])
    
    # Determine the range index based on years of education and experience
    if state[0] < 4: #education
        x = 0
    elif state[0] < 6:
        x = 1
    elif state[0] < 8:
        x = 2
    else:
        x = 3

    if state[1] < 5: #experience
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
            - Years of education (int) idx 0
            - Years of experience (int) idx 1
            - Total savings (int) idx 2
            - Age (int) idx 3
        action (int): The action to be taken, where 0 represents no action and 1 represents advancing education.

    Returns:
        list of tuples: A list containing tuples representing possible next states and their probabilities.
    """
    poss_salary1 = get_salary(state,action)
    poss_salary2 = get_salary(state,action)

    # Define the cost of living
    cost_of_living = 30000

    savings = state[2]

    # interest calculation
    if savings < 0:
        savings *= -1.065
    else:
        # growth between 3 & 9%
        savings *= 1 + random.random() * 0.06 + 0.03

    # round savings to the nearest 1000
    savings = round(savings, -3)

    if action == 1:
        # If action is to advance education, subtract education cost from savings
        total_savings1 = savings - 20000 + poss_salary1
        total_savings2 = savings - 20000 + poss_salary2

        years_edu = state[0] + 1
        years_exp = state[1]
    else:
        # If no action is taken, add salary to savings
        total_savings1 = savings + poss_salary1
        total_savings2 = savings + poss_salary2
        years_exp = state[1] + 1
        years_edu = state[0]
    
    # Create possible next states
    state1 = (years_edu, years_exp, total_savings1 - cost_of_living, state[3] + 1)
    state2 = (years_edu, years_exp, total_savings2 - cost_of_living, state[3] + 1)

    # Return possible next states with equal probabilities
    return [(0.5, state1),
            (0.5, state2)]

def reward(state, action, loe, smug, handy):
    """
    Calculate the reward based on the current state and action.

    Args:
        state (tuple): A tuple representing the current state, containing:
            - Years of education (int) idx 0 
            - Years of experience (int) idx 1
            - Total savings (int) idx 2
            - Age (int) idx 3
        action (int): The action taken, where 0 represents no action and 1 represents advancing education.
        loe (float): love for education, can be thought of as the utility of 1 year of education
        smug (float): smugness factor, can be thought of as a value for holding the degree for 1 year or a lifestyle preference
        handy (float): handyman factor, can be thought of as a value for working with ones hands and or perfecting a craft based on yoe

    Returns:
        int: The reward, which is the current total savings.
    """
    # TODO could modify the reward function to shape preferences
    immediate_reward = state[2] #reward is initially based on savings
    if action == 1: # If action is to advance education, add love for education to reward 
        immediate_reward += loe * 1e4
    if state[0] >= 8:
        immediate_reward += smug * 8e4 # we have a phd, add smugness factor to reward
    elif state[0] >= 6:
        immediate_reward += smug * 4e4 # we have a masters, add smugness factor to reward
    elif state[0] >= 4:
        immediate_reward += smug * 1e4 # we have a bachelors, add smugness factor to reward

    if state[0] <=4: #you only get the handyman reward if you didn't finish college. if finish college, get desk job
        if state[1] >= 20: 
            immediate_reward += handy * 4e4 # we have 20 years of experience, add handyman factor to reward
        elif state[1] >= 15:
            immediate_reward += handy * 3e4 # we have 15 years of experience, add handyman factor to reward
        elif state[1] >= 10:
            immediate_reward += handy * 2e4
        elif state[1] >= 5:
            immediate_reward += handy * 1e4
        return immediate_reward

def available_actions(state):
    """
    Determine the available actions based on the current state.

    Args:
        state (tuple): A tuple representing the current state, containing:
            - Years of education (int) idx 0 
            - Years of experience (int) idx 1
            - Total savings (int) idx 2
            - Age (int) idx 3

    Returns:
        list: A list containing available actions, where 0 represents no (relevant) action (go to work) and 1 represents advancing education.
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
            - Years of education (int) idx 0 
            - Years of experience (int) idx 1
            - Total savings (int) idx 2
            - Age (int) idx 3

    Returns:
        tuple: A tuple containing a boolean indicating if the state is terminal and, if so, the terminal return.
    """
    # Terminal state reached at age 65
    if state[3] >= 65:
        return True, (state[2], -1)  # Return savings and a special action value indicating terminal state
    else:
        return False, ()

cache = {}

def bellman(state, loe, smug, handy):
    """
    Apply the Bellman equation to find the optimal action and value for a given state.

    Args:
        state (tuple): A tuple representing the current state, containing:
            - Years of education (int) idx 0 
            - Years of experience (int) idx 1
            - Total savings (int) idx 2
            - Age (int) idx 3
        loe (float): love for education, can be thought of as the utility of 1 year of education
        smug (float): smugness factor, can be thought of as a value for holding the degree for 1 year or a lifestyle preference
        handy (float): handyman factor, can be thought of as a value for working with ones hands, for people who did not finish college

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
            exp_action_value += p_state * (reward(state, 
                                                  action,
                                                  loe,
                                                  smug,
                                                  handy) 
                                            + bellman(next_state,
                                                      loe,
                                                      smug,
                                                      handy)[0])
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

def optimal_career_path_to_df(start_state, loe = 0, smug = 0, handy = 0):
    """
    Simulate a career path based on a start state using the Bellman equation.

    Args:
        start_state (tuple): Initial state tuple (Years of Education, Years of Experience, Total Savings, Age)
        loe (float): love for education, can be thought of as the utility of 1 year of education
        smug (float): smugness factor, can be thought of as a value for holding the degree for 1 year or a lifestyle preference

    Returns:
        DataFrame: A pandas DataFrame containing the simulated career path.
    """
    state = start_state
    state_actions = []
    
    while not terminal_state(state)[0]:
        best_value, best_action = bellman(state, loe, smug, handy)
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

