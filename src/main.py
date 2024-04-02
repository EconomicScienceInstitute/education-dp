from education_model import optimize_education
from career_model import recommend_career
from utils import load_data

def main():
    # Collect user inputs
    user_preferences = {}  # Placeholder for user input collection
    education_data, career_data = load_data()

    # Process inputs through models
    education_path = optimize_education(user_preferences, education_data)
    career_path = recommend_career(user_preferences, career_data)

    # Display results (Placeholder for console-based output)
    print("Recommended Education Path:", education_path)
    print("Recommended Career Path:", career_path)

if __name__ == "__main__":
    main()