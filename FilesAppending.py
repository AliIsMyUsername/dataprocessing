import os
import pandas as pd

# Directory containing the CSV files
folder_path = r'E:\Data_V3\Data\S11\Combined\New folder'

# Output file where the combined data will be saved
output_file = 'S11_4&8&16&32R.csv'

# List to hold all the dataframes
dataframes = []

# Iterate over all the CSV files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):  # Process only CSV files
        file_path = os.path.join(folder_path, filename)
        # Read each CSV file into a dataframe
        df = pd.read_csv(file_path)
        dataframes.append(df)

# Concatenate all dataframes
combined_df = pd.concat(dataframes, ignore_index=True)

# Save the combined dataframe to a new CSV file
combined_df.to_csv(output_file, index=False)

print(f"All files have been combined and saved to {output_file}")
