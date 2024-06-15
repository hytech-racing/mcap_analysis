import pandas as pd

def monitor_and_split(df, columns_to_monitor):
    # Store initial values of the monitored columns
    initial_values = df[columns_to_monitor].iloc[0].copy()
    # List to store the derived DataFrames
    derived_dataframes = []
    # Start index for slicing DataFrame
    start_idx = 0
    
    # Iterate over the DataFrame rows
    for idx, row in df.iterrows():
        # Check if there is any change in the monitored columns
        if not row[columns_to_monitor].equals(initial_values):
            # If there's a change, slice the DataFrame from start index to current index
            derived_df = df.iloc[start_idx:idx].copy()
            # Add the derived DataFrame to the list
            derived_dataframes.append(derived_df)
            # Update the initial values to the current row values
            initial_values = row[columns_to_monitor].copy()
            # Update the start index to current index
            start_idx = idx
    
    # Handle the last segment
    if start_idx < len(df):
        derived_df = df.iloc[start_idx:].copy()
        derived_dataframes.append(derived_df)
    
    return derived_dataframes

# Example usage
data = {
    'A': [1, 1, 2, 2, 3, 3, 4],
    'B': [10, 10, 20, 20, 30, 30, 40],
    'C': [100, 100, 100, 200, 200, 300, 300]
}

df = pd.DataFrame(data)
columns_to_monitor = ['A', 'B']
derived_dfs = monitor_and_split(df, columns_to_monitor)

# Output the derived DataFrames
for i, derived_df in enumerate(derived_dfs):
    print(f"Derived DataFrame {i+1}:\n{derived_df}\n")
