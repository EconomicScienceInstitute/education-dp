def recommend_career(preferences, data, preferred_industry=None):
    """
    Recommend an optimal career based on user preferences and available data.

    This function filters the available data based on the user's minimum salary preference and preferred industry,
    if specified. It then calculates a satisfaction ratio for each career option by dividing the job satisfaction
    rating by the salary. The career with the highest satisfaction ratio is selected as the optimal career.

    Parameters:
    - preferences (dict): A dictionary containing user preferences, including minimum salary.
    - data (DataFrame): A pandas DataFrame containing career data, including salary and satisfaction ratings.
    - preferred_industry (str, optional): The user's preferred industry. Defaults to None.

    Returns:
    - str: The name of the optimal career based on the calculated satisfaction ratio.
    """
    # Example criteria from preferences
    min_salary = preferences.get('min_salary', 0)
    
    # Filter data based on preferences
    filtered_data = data[(data['salary'] >= min_salary)]
    if preferred_industry:
        filtered_data = filtered_data[filtered_data['industry'] == preferred_industry]
    
    # Placeholder for dynamic programming algorithm
    # For simplicity, we select the career with the highest job satisfaction rating
    filtered_data['satisfaction_ratio'] = filtered_data['satisfaction'] / filtered_data['salary']
    optimal_career = filtered_data.loc[filtered_data['satisfaction_ratio'].idxmax()]
    
    return optimal_career['career']
