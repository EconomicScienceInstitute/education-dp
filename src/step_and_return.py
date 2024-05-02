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
  
  salary = random.randint(min_salary[x, y], max_salary[x, y])
  return salary

def step(state, action):
  this_years_salary = get_salary(state)
  total_savings = state[2] + this_years_salary
  if action == 1:
    total_savings -= 20000
    years_edu = state[0] + 1
    years_exp = state[1]
  else:
    years_exp = state[1] + 1
    years_edu = state[0]

  # return state
  return (years_edu, years_exp, total_savings)

def reward(state, action):
  # return the current savings
  return state[2]
