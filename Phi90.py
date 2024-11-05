import pandas as pd
import os
import re

# Base folder path
base_path = r'E:\Data_V3\Data\04Rx16C\phi90'

# Loop through numbers and construct paths
for i in range(1, 2):
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
    print(param_values)
    Theta = []
    Phi = []
    AbsDir = []
    with open(file_path, 'r') as file:
        data_section = None  # Track which section (S2, S3, ...) we're processing
        for line in file:
            # Detect start of data sections for S2 to S31
            if line.strip() == "farfield (f=20)":
                # Toggle to next section (S2 to S31) after encountering each separator
                if data_section is None:
                    data_section = 'Theta'
                elif data_section == 'Theta':
                    data_section = 'Phi'
                elif data_section == 'Phi':
                    data_section = 'Abs(Dir.)'
                continue

            parts = line.strip().split()
            if len(parts) == 2:  # Ensure line has exactly two elements
                freq = float(parts[0])  # Frequency in GHz
                if data_section == 'Theta':
                    s2_mag = float(parts[1])  # S2 magnitude in dB
                    frequencies.append(freq)
                    Theta.append(s2_mag)
                elif data_section == 'Phi':
                    s3_mag = float(parts[1])  # S3 magnitude in dB
                    Phi.append(s3_mag)
                elif data_section == 'Abs':
                    s4_mag = float(parts[1])  # S4 magnitude in dB
                    AbsDir.append(s4_mag)
    df9 = pd.DataFrame({'S9 Magnitude (dB)': AbsDir})
    print(df9)