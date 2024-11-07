import pandas as pd
import os
import re

# Base folder path
base_path = r'E:\Data_V3\Data\04Rx16C\phi90'

# Loop through numbers and construct paths
for i in range(1,2 ):
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
print(param_values)
#####################################################################################################################################
    # with open(file_path, 'r') as file:
    #     lines = file.readlines()
    #
    # # Assuming the text file has space-separated data, split each line into columns
    # data = [line.strip().split() for line in lines]
    #
    # # Convert to a DataFrame
    # df = pd.DataFrame(data)
    #
    # # Save to CSV
    # df = df.iloc[:, :-61]
    # df = df[~df.apply(lambda row: row.astype(str).str.contains('#Parameters|Theta')).any(axis=1)]
    # separator1='------------------------------------------------------------------------------------------------------------------------------------------------------'
    # df = df[~df.apply(lambda row: row.astype(str).str.contains(separator1)).any(axis=1)]
    # # Drop rows where all values are None (or NaN)
    # df = df.dropna(how='all')
    # # df.insert(0, 'New_Column', 0)
    #
    # # Print the row at index 5
    # # print(df.iloc[360])
    # # print(df.iloc[361])
    # # print(df.iloc[362])
    # # print(df.iloc[363])
    # # print(df.iloc[364])
    # # print(df.iloc[365])
    # csv_file_path = r'E:\Data_V3\Data\04Rx16C\phi90\output_V1.csv'
    # df.to_csv(csv_file_path, index=False, header=False)
    # print(df.head())
    #
    # for index, row in df.iterrows():
    #     # Check if the 'Farfield' column contains a frequency pattern like '(f=20)'
    #     if isinstance(row[1], str) and row[1].startswith('(f='):
    #         current_frequency = row[1]  # Update current frequency value
    #
    #     # Assign the current frequency to a new column
    #     df.loc[index, 'Frequency (GHz)'] = current_frequency
    #
    # columns = ['Frequency (GHz)'] + [col for col in df.columns if col != 'Frequency (GHz)']
    # df = df[columns]
    # # Display the updated DataFrame
    #
    # df = df[~df.apply(lambda row: row.astype(str).str.contains('farfield', case=False)).any(axis=1)]
    # column_names = ['Frequency (GHz)', 'Theta', 'Phi', 'Abs(Dir.)']  # Adjust as per your data
    # # Assign the column names to the DataFrame
    # df.columns = column_names
    # for param, value in param_values.items():
    #     df.insert(0, param, value)
    # df.insert(0, 'C', 16)  # Insert 'C' as 32
    # df.insert(0, 'R', 4)   # Insert 'R' as 4
    # print(df)
    # csv_file_path = r'E:\Data_V3\Data\04Rx16C\phi90\output_V2.csv'
    # df.to_csv(csv_file_path, index=False, header=True)
#####################################################################################################################################################
    # pattern = r'\(f=\d+(\.\d+)?\)'
    #
    # # Filter rows that contain the frequency pattern in any column
    # f_rows = df[df.apply(lambda row: row.astype(str).str.contains(pattern)).any(axis=1)]
    # f_rows = f_rows.iloc[:, :-6]
    # f_rows = f_rows.drop(f_rows.columns[0], axis=1)
    # f_rows = f_rows.drop(f_rows.columns[0], axis=1)
    #
    # print(f_rows)
    # csv_file_path = r'E:\Data_V3\Data\04Rx16C\phi90\freq.csv'
    # f_rows.to_csv(csv_file_path, index=False, header=False)

    # df = df[~df['0'].str.startswith("#Parameters")].reset_index(drop=True)
    # targetWord='------------------------------------------------------------------------------------------------------------------------------------------------------'
    # df = df[~df['0'].str.startswith(targetWord)].reset_index(drop=True)
    # csv_file_path = r'E:\Data_V3\Data\04Rx16C\phi90\output_V2.csv'
    # df.to_csv(csv_file_path, index=False, header=False)
    # # Display the modified DataFrame
    # print(df.head())

    # print("File has been converted to CSV and saved.")
