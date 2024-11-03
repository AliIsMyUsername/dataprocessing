import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
import seaborn as sns
from matplotlib.ticker import FuncFormatter
import re

# Base folder path
base_path = r'E:\Data_V3\Data\04Rx16C\s11'
# file_path = r'E:\Data_V3\Data\04Rx16C\s11\1.txt'
# Loop through numbers and construct paths
for i in range(1, 91):
    file_path = os.path.join(base_path, f"{i}.txt")


    # Parameters to search for
    params = [" a", " a_B", " d", " h", " h_B", " HL"]

    # Dictionary to store parameter values
    param_values = {}

    # Read the file and search for parameters
    with open(file_path, 'r') as file:
        content = file.read()
        for param in params:
            # Regular expression to find the parameter and its value
            match = re.search(rf"{param}=(\d+\.?\d*);", content)
            if match:
                param_values[param] = float(match.group(1))

    # Print the found parameter values

    # Lists to store frequencies, S2 magnitudes, and S3 magnitudes
    frequencies = []
    s2_magnitudes = []
    s3_magnitudes = []

    # Read the file and parse the data sections
    with open(file_path, 'r') as file:
        data_section = None  # None = Not started, 'S2' = S2 section, 'S3' = S3 section
        for line in file:
            # Detect start of data sections
            if line.strip() == "#-----------------------------------------------":
                # Toggle between S2 and S3 sections after encountering each separator
                data_section = 'S2' if data_section is None else 'S3'
                continue

            # Process S2 data section (frequency and S2 magnitude)
            if data_section == 'S2':
                parts = line.strip().split()
                if len(parts) == 2:  # Ensure line has exactly two elements
                    freq = float(parts[0])  # Frequency in GHz
                    s2_mag = float(parts[1])  # S2 magnitude in dB
                    frequencies.append(freq)
                    s2_magnitudes.append(s2_mag)

            # Process S3 data section (only S3 magnitude)
            elif data_section == 'S3':
                parts = line.strip().split()
                if len(parts) == 2:  # Ensure line has exactly two elements
                    s3_mag = float(parts[1])  # S3 magnitude in dB
                    s3_magnitudes.append(s3_mag)

    # Create a DataFrame from the lists
    df = pd.DataFrame({
        'Frequency (GHz)': frequencies,
        'S2 Magnitude (dB)': s2_magnitudes,
        'S3 Magnitude (dB)': s3_magnitudes
    })
    for param, value in param_values.items():
        # print(f"{param} = {value}")
        df.insert(0, param, value)
    df.insert(0, 'C', 16)
    df.insert(0, 'R', 4)
    df['S Average '] = df.iloc[:, -2:].mean(axis=1)
    df.drop(df.columns[-3:-1], axis=1, inplace=True)
    # Display the DataFrame
    # print(df)

    # Optionally, save the DataFrame to a CSV file
    savePath=os.path.join(base_path, f"{i}.csv")
    df.to_csv(savePath, index=False)
git 

