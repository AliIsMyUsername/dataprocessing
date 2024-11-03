import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
import seaborn as sns
from matplotlib.ticker import FuncFormatter
import re



file_path = r'E:\Data_V3\Data\04Rx16C\s11\1.txt'

# Parameters to search for
# params = [" a", " a_B", " d", " h", " h_B", " HL"]
#
# # Dictionary to store parameter values
# param_values = {}
#
# # Read the file and search for parameters
# with open(file_path, 'r') as file:
#     content = file.read()
#     for param in params:
#         # Regular expression to find the parameter and its value
#         match = re.search(rf"{param}=(\d+\.?\d*);", content)
#         if match:
#             param_values[param] = float(match.group(1))
#
# # Print the found parameter values
# for param, value in param_values.items():
#     print(f"{param} = {value}")

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

# Display extracted data
# for freq, s2_mag, s3_mag in zip(frequencies, s2_magnitudes, s3_magnitudes):
#     print(f"Frequency: {freq} GHz, S2 Magnitude: {s2_mag} dB, S3 Magnitude: {s3_mag} dB")