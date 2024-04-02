---
runme:
  id: 01HTE2YC8TJZCJN4M4JKWB09S3
  version: v3
---

# education-dp

# *EduDynamic* (tentative name)

The EduDynamic project aims to model and optimize education and career planning decisions using dynamic programming. It will allow users to input their personal preferences, financial constraints, and career goals to receive tailored advice on education paths, potential investments, and career choices.

## Project Structure

```
EduDynamic/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── education_model.py
│   ├── career_model.py
│   ├── optimization.py
│   └── utils.py
│
├── tests/
│   ├── __init__.py
│   ├── test_education_model.py
│   ├── test_career_model.py
│   └── test_optimization.py
│
├── data/
│   ├── education_data.csv
│   └── career_data.csv
│
├── docs/
│   └── project_documentation.md
│
├── requirements.txt
└── README.md
```

## File Descriptions

- `src/__init__.py`: Initializes the source code directory as a Python package.
- `src/main.py`: The entry point of the application. It will handle user inputs and display outputs based on the models' advice.
- `src/education_model.py`: Contains the dynamic programming model for optimizing education decisions, including choosing majors, deciding between trade school and university, etc.
- `src/career_model.py`: Contains the dynamic programming model for career planning, including job transitions, retirement planning, etc.
- `src/optimization.py`: Implements the optimization algorithms used in the education and career models.
- `src/utils.py`: Utility functions used across the project, such as data loading and preprocessing.
- `tests/__init__.py`: Initializes the tests directory as a Python package.
- `tests/test_*.py`: Unit tests for each corresponding module in src/.
- `data/`: Contains CSV files with data on education paths and career options.
- `docs/project_documentation.md`: Detailed documentation of the project, including the models' assumptions, limitations, and usage instructions.
- `requirements.txt`: Lists all Python libraries required by the project.
- `README.md`: Provides an overview of the project, installation instructions, and basic usage examples.

## Project Design

### Target Input/Output

The EduDynamic project is designed to take user inputs regarding their personal preferences, financial constraints, career goals, and educational aspirations to provide a tailored, dynamic plan for education and career progression. Here's an overview of the target input and output for the project:

#### Input

Users will provide the following information through an interactive interface:

- **Basic Information**: Current age, current stage (e.g., High School, Undergraduate), and years in the current stage.
- **Education Preferences**: Plans for pursuing undergraduate and/or graduate degrees, fields of study, and anticipated duration for each degree.
- **Career Preferences**: Preferred industries, job roles, and minimum salary expectations.
- **Lifestyle and Financial Stability Preferences**: Desired retirement age, lifestyle expectations, and vacation frequency.

#### Output

Based on the inputs, the project will output:

- **Optimal Education Path**: Recommendations for education paths, including the type of degree, field of study, and institutions, tailored to the user's preferences and constraints.
- **Career Planning**: Career options that align with the user's education, preferred industry, and salary expectations.
- **Comprehensive Life Plan**: A detailed plan that integrates education, career, and retirement planning, offering a roadmap from the current stage to retirement.

### Implementation Details

The project utilizes dynamic programming algorithms implemented in Python to optimize the decision-making process. Key components include:

- **Data Models**: The project dynamically generates data based on real-time user inputs directly within the application.
- **Optimization Algorithms**: Implemented in `src/optimization.py`, these algorithms consider various paths and choices to recommend the most beneficial plan based on the user's inputs.
- **User Interface**: Built with Streamlit (`src/main.py`), the interface collects user inputs and uses them directly for optimization.

### Example Usage

After running the application, users will be prompted to enter their information and preferences. The application will then process this data and display an optimal life plan, including education and career recommendations, tailored to the user's specific goals and constraints.
