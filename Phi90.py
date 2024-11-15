import pandas as pd
import os
import re

# Base folder path
base_path = r'E:\Data_V3\Data\32Rx32C\phi90'

# Loop through numbers and construct paths
for i in range(1,91):
    file_path = os.path.join(base_path, f"{i}.txt")

    # Parameters to search for
    params = [" a", " a_B", " d", " h", " h_B", " HL"]

    # Dictionary to store parameter values
    param_values = {}
    with open(file_path, 'r') as file:
        content = file.read()
        for param in params:
            # Regular expression to find the parameter and its value
            match = re.search(rf"{param}=(\d+\.?\d*);", content)
            if match:
                param_values[param] = float(match.group(1))
    # print(param_values)

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Assuming the text file has space-separated data, split each line into columns
    data = [line.strip().split() for line in lines]

    # Convert to a DataFrame
    df = pd.DataFrame(data)

    # Save to CSV
    df = df.iloc[:, :-61]
    df = df[~df.apply(lambda row: row.astype(str).str.contains('#Parameters|Theta')).any(axis=1)]
    separator1='------------------------------------------------------------------------------------------------------------------------------------------------------'
    df = df[~df.apply(lambda row: row.astype(str).str.contains(separator1)).any(axis=1)]
    # Drop rows where all values are None (or NaN)
    df = df.dropna(how='all')

    # csv_file_path = r'E:\Data_V3\Data\04Rx16C\phi90\output_V1.csv'
    # df.to_csv(csv_file_path, index=False, header=False)
    # print(df.head())

    for index, row in df.iterrows():
        # Check if the 'Farfield' column contains a frequency pattern like '(f=20)'
        if isinstance(row[1], str) and row[1].startswith('(f='):
            current_frequency = row[1]  # Update current frequency value

        # Assign the current frequency to a new column
        df.loc[index, 'Frequency (GHz)'] = current_frequency

    columns = ['Frequency (GHz)'] + [col for col in df.columns if col != 'Frequency (GHz)']
    df = df[columns]
    # Display the updated DataFrame

    df = df[~df.apply(lambda row: row.astype(str).str.contains('farfield', case=False)).any(axis=1)]
    column_names = ['Frequency (GHz)', 'Theta', 'Phi', 'Abs(Dir.)']  # Adjust as per your data
    # Assign the column names to the DataFrame
    df.columns = column_names
    for param, value in param_values.items():
        df.insert(0, param, value)
    df.insert(0, 'C', 32)  # Insert 'C' as 32
    df.insert(0, 'R', 32)   # Insert 'R' as 4
    # print(df)
    # csv_file_path = r'E:\Data_V3\Data\04Rx16C\phi90\output_V2.csv'
    # df.to_csv(csv_file_path, index=False, header=True)
    savePath = os.path.join(base_path, f"{i}.csv")
    df.to_csv(savePath, index=False, header=True)
