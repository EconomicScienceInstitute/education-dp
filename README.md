---
runme:
  id: 01HTE2YC8TJZCJN4M4JKWB09S3
  version: v3
---

# education-dp

# *EduDynamic*

The EduDynamic project aims to model and optimize education and career planning decisions using dynamic programming. It will allow users to input their personal preferences, financial constraints, and career goals to receive tailored advice on education paths, potential investments, and career choices.

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
`src/__init__.py`: Initializes the source code directory as a Python package.
`src/main.py`: The entry point of the application. It will handle user inputs and display outputs based on the models' advice.
`src/education_model.py`: Contains the dynamic programming model for optimizing education decisions, including choosing majors, deciding between trade school and university, etc.
`src/career_model.py`: Contains the dynamic programming model for career planning, including job transitions, retirement planning, etc.
`src/optimization.py`: Implements the optimization algorithms used in the education and career models.
`src/utils.py`: Utility functions used across the project, such as data loading and preprocessing.
`tests/__init__.py`: Initializes the tests directory as a Python package.
`tests/test_*.py`: Unit tests for each corresponding module in src/.
`data/`: Contains CSV files with data on education paths and career options.
`docs/project_documentation.md`: Detailed documentation of the project, including the models' assumptions, limitations, and usage instructions.
`requirements.txt`: Lists all Python libraries required by the project.
`README.md`: Provides an overview of the project, installation instructions, and basic usage examples.