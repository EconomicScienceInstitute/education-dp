import math
import numpy as np
import random
def get_salary(state):
  min_salary = np.array([[24, 30, 40, 55, 85],
                [45, 60, 70, 80, 100],
                [70, 85, 95, 105, 125],
                [85, 95, 115, 135, 150]])
  max_salary = np.array([[27, 38, 50, 85, 150],
                [60, 70, 100, 120, 200],
                [85, 100, 110, 125, 225],
                [95, 120, 135, 160, 300]])
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
  
  salary = random.randint(min_salary[x, y], max_salary[x, y])*1000
  return salary

def possible_states(state, action):
  poss_salary1 = get_salary(state)
  poss_salary2 = get_salary(state)

  cost_of_living = 30000

  if action == 1:
    total_savings1 = state[2] - 20000 + poss_salary1
    total_savings2 = state[2] - 20000 + poss_salary2

    years_edu = state[0] + 1
    years_exp = state[1]
  else:
    total_savings1 = state[2] + poss_salary1
    total_savings2 = state[2] + poss_salary2
    years_exp = state[1] + 1
    years_edu = state[0]
  # state[3] + 1 adds one year to age for terminal state purposes
  state1 = (years_edu, years_exp, total_savings1-cost_of_living, state[3] + 1)
  state2 = (years_edu, years_exp, total_savings2-cost_of_living, state[3] + 1)

  # return state
  return [(0.5, state1),
          (0.5, state2)]

def reward(state, action):
  # return the current savings
  return state[2]

def available_actions(state):
  return [0, 1]

def terminal_state(state):
  if state[3] >= 65:
    return True, (state[2], -1)
  else:
    return False, ()

cache = {}
def bellman(state):
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
      exp_action_value += p_state*(reward(state, action) + bellman(next_state)[0])
    if best_value is None or exp_action_value > best_value:
      best_value = exp_action_value
      best_action = action
  cache[state] = (best_value, best_action)
  return best_value, best_action

# example bellman
print(bellman((0, 0, 0, 18)))