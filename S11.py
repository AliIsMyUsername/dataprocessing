import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
import seaborn as sns
from matplotlib.ticker import FuncFormatter
import re

# Base folder path
base_path = r'E:\Data_V3\Data\08Rx16C\s11'
# Loop through numbers and construct paths
for i in range(10, 89):
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

    # Lists to store frequencies and S-magnitudes (S2 to S7)
    frequencies = []
    s2_magnitudes = []
    s3_magnitudes = []
    s4_magnitudes = []
    s5_magnitudes = []
    s6_magnitudes = []
    s7_magnitudes = []

    # Read the file and parse the data sections
    with open(file_path, 'r') as file:
        data_section = None  # Track which section (S2, S3, ...) we're processing
        for line in file:
            # Detect start of data sections for S2 to S7
            if line.strip() == "#-----------------------------------------------------------------------------------------------------------------------------":
                # Toggle to next section (S2 to S7) after encountering each separator
                if data_section is None:
                    data_section = 'S2'
                elif data_section == 'S2':
                    data_section = 'S3'
                elif data_section == 'S3':
                    data_section = 'S4'
                elif data_section == 'S4':
                    data_section = 'S5'
                elif data_section == 'S5':
                    data_section = 'S6'
                elif data_section == 'S6':
                    data_section = 'S7'
                continue

            # Process the respective data sections (frequency and magnitude)
            parts = line.strip().split()
            if len(parts) == 2:  # Ensure line has exactly two elements
                freq = float(parts[0])  # Frequency in GHz
                if data_section == 'S2':
                    s2_mag = float(parts[1])  # S2 magnitude in dB
                    frequencies.append(freq)
                    s2_magnitudes.append(s2_mag)
                elif data_section == 'S3':
                    s3_mag = float(parts[1])  # S3 magnitude in dB
                    s3_magnitudes.append(s3_mag)
                elif data_section == 'S4':
                    s4_mag = float(parts[1])  # S4 magnitude in dB
                    s4_magnitudes.append(s4_mag)
                elif data_section == 'S5':
                    s5_mag = float(parts[1])  # S5 magnitude in dB
                    s5_magnitudes.append(s5_mag)
                elif data_section == 'S6':
                    s6_mag = float(parts[1])  # S6 magnitude in dB
                    s6_magnitudes.append(s6_mag)
                elif data_section == 'S7':
                    s7_mag = float(parts[1])  # S7 magnitude in dB
                    s7_magnitudes.append(s7_mag)

    # Create a DataFrame from the lists
    df = pd.DataFrame({
        'Frequency (GHz)': frequencies,
        'S2 Magnitude (dB)': s2_magnitudes,
        'S3 Magnitude (dB)': s3_magnitudes,
        'S4 Magnitude (dB)': s4_magnitudes,
        'S5 Magnitude (dB)': s5_magnitudes,
        'S6 Magnitude (dB)': s6_magnitudes,
        'S7 Magnitude (dB)': s7_magnitudes
    })

    # Add parameter values as columns in the DataFrame
    for param, value in param_values.items():
        df.insert(0, param, value)
    df.insert(0, 'C', 16)  # Insert 'C' as 32
    df.insert(0, 'R', 8)   # Insert 'R' as 4

    # Calculate the average of S2 to S7 and add it as a new column
    df['S Average'] = df.iloc[:, -6:].mean(axis=1)
    df.drop(df.columns[-7:-1], axis=1, inplace=True)

    # Optionally, save the DataFrame to a CSV file
    savePath = os.path.join(base_path, f"{i}.csv")
    df.to_csv(savePath, index=False)
