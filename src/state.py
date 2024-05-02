from src.action_space import Job, actions

class State:
    """
    Represents the state of an individual in the simulation, including both static and stochastic attributes.
    """
    def __init__(self, age, education_level, years_in_education, years_of_experience, savings, retirement_age, inflation_rate, investment_return_rate, salary):
        """
        Initialize the state of an individual with given parameters.
        
        Parameters:
        - age (int): Current age of the individual.
        - education_level (str): Highest level of education achieved.
        - years_in_education (int): Total years spent in education.
        - years_of_experience (int): Total years of work experience.
        - savings (float): Current amount of savings, modified by education/work status.
        - retirement_age (int): Age at which the individual plans to retire.
        - inflation_rate (float): Annual inflation rate.
        - investment_return_rate (float): Annual return rate from investments.
        - salary (float): Current salary, subject to stochastic changes.
        """
        self.age = age
        self.education_level = education_level
        self.years_in_education = years_in_education
        self.years_of_experience = years_of_experience  # Track years of experience
        self.savings = savings  # Initialize savings, modified by education/work status
        self.retirement_age = retirement_age
        self.inflation_rate = inflation_rate
        self.investment_return_rate = investment_return_rate
        self.salary = salary  # Stochastic element that can change based on job performance

    def update_savings_from_job(self, annual_salary):
        self.savings += annual_salary  # Increase savings by the salary amount

    def update_savings_from_education(self, annual_cost):
        self.savings -= annual_cost  # Decrease savings by the cost of education

    def simulate_year(self, action):
        if action.type == 'work':
            self.update_savings_from_job(action.salary)
            self.years_of_experience += 1
        elif action.type == 'study':
            self.update_savings_from_education(action.cost)
            self.years_in_education += 1

    def calculate_salary(self):
        base_salary = self.salary
        # Add logic to adjust salary based on education and experience
        return base_salary + (self.years_of_experience * 1000) + (self.years_in_education * 500)

    def __repr__(self):
        """
        Provides a formal string representation of the State object for debugging and logging.

        This method returns a formatted string that includes all the attributes of the State instance with their respective values,
        making it easier to understand the current state of an object when printed or logged.
        """
        return f"State(age={self.age}, education_level='{self.education_level}', years_in_education={self.years_in_education}, 
        years_of_experience={self.years_of_experience}, savings={self.savings}, retirement_age={self.retirement_age}, 
        inflation_rate={self.inflation_rate}, investment_return_rate={self.investment_return_rate}, salary={self.salary})"
class Parameters:
    """
    Holds the parameters for the simulation, including options for education and career, and transition probabilities.
    """
    def __init__(self, education_options, career_options, lifestyle_preferences, transition_probabilities):
        """
        Initialize the parameters for the simulation.
        
        Parameters:
        - education_options (list): Education paths available.
        - career_options (list): Career options available.
        - lifestyle_preferences (tuple): Lifestyle and vacation preferences.
        - transition_probabilities (dict): Probabilities for different state transitions.
        """
        self.education_options = education_options  # List of tuples (degree, field, duration)
        self.career_options = career_options  # List of tuples (industry, role, min_salary)
        self.lifestyle_preferences = lifestyle_preferences  # Tuple (lifestyle_expectation, vacation_frequency)
        self.transition_probabilities = transition_probabilities  # Dictionary to handle stochastic transitions

    def __repr__(self): 
        """
        Provides a string representation of the Parameters instance.

        This method is used to create a human-readable string that describes the instance of the Parameters class. It includes all the attributes such as education options, career options, lifestyle preferences, and transition probabilities. This representation is helpful for debugging and logging the state of Parameters objects.
        """
        return f"Parameters(education_options={self.education_options}, career_options={self.career_options}, lifestyle_preferences={self.lifestyle_preferences}, transition_probabilities={self.transition_probabilities})"

def bellman_equation(state, parameters, jobs, education):
    """
    Computes the optimal decision for the next state using the Bellman equation.
    
    Parameters:
        state (State): Current state of the individual.
        parameters (Parameters): Simulation parameters.
        jobs (list): List of possible jobs.
        education (list): List of possible education paths.
    
    Returns:
        tuple: Optimal action and the expected value of taking that action.
    """
    possible_actions = actions(state, jobs, education)
    # Placeholder logic to calculate the next state based on transition probabilities
    # This should be replaced with actual decision-making logic based on the Bellman equation
    if possible_actions:
        # Example: Select the first action as the optimal one (this is just a placeholder)
        optimal_action = possible_actions[0]
        expected_value = 0  # Placeholder for expected value calculation
        return optimal_action, expected_value
    else:
        return None, None  # Return None if no possible actions are available

# Example use case

# sample data for jobs and education paths
jobs = [
    Job(salary=50000, education_requirements='Bachelor', work_requirements=2, low_raise=1000, high_raise=5000, years_in=2),
    Job(salary=80000, education_requirements='Master', work_requirements=5, low_raise=2000, high_raise=7000, years_in=5)
]

education_paths = [
    ('Bachelor', 'Engineering', 4),
    ('Master', 'Engineering', 2)
]

# Define the initial state of an individual
initial_state = State(
    age=25,
    education_level='High School',
    years_in_education=12,
    years_of_experience=0,
    savings=0,
    retirement_age=65,
    inflation_rate=0.02,
    investment_return_rate=0.05,
    salary=30000
)

# Define the parameters for the simulation
simulation_parameters = Parameters(
    education_options=education_paths,
    career_options=[('Tech', 'Software Engineer', 50000)],
    lifestyle_preferences=('Moderate', 2),
    transition_probabilities={'promotion': 0.2, 'job_change': 0.3, 'further_education': 0.1}
)

# Use the bellman_equation function to determine the optimal action and its expected value
optimal_action, expected_value = bellman_equation(initial_state, simulation_parameters, jobs, education_paths)

# Print the results
print("Optimal Action:", optimal_action)
print("Expected Value of Optimal Action:", expected_value)
