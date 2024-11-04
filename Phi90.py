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