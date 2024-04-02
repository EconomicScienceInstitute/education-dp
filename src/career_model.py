def recommend_career(preferences, data, preferred_industry=None):
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
