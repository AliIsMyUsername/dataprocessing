import pandas as pd
import os
import re

# Base folder path
base_path = r'E:\Data_V3\Data\32Rx32C\s11'

# Loop through numbers and construct paths
for i in range(10, 91):
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

    # Lists to store frequencies and S-magnitudes (S2 to S31)
    frequencies = []
    s2_magnitudes = []
    s3_magnitudes = []
    s4_magnitudes = []
    s5_magnitudes = []
    s6_magnitudes = []
    s7_magnitudes = []
    s8_magnitudes = []
    s9_magnitudes = []
    s10_magnitudes = []
    s11_magnitudes = []
    s12_magnitudes = []
    s13_magnitudes = []
    s14_magnitudes = []
    s15_magnitudes = []
    s16_magnitudes = []
    s17_magnitudes = []
    s18_magnitudes = []
    s19_magnitudes = []
    s20_magnitudes = []
    s21_magnitudes = []
    s22_magnitudes = []
    s23_magnitudes = []
    s24_magnitudes = []
    s25_magnitudes = []
    s26_magnitudes = []
    s27_magnitudes = []
    s28_magnitudes = []
    s29_magnitudes = []
    s30_magnitudes = []
    s31_magnitudes = []

    # Read the file and parse the data sections
    with open(file_path, 'r') as file:
        data_section = None  # Track which section (S2, S3, ...) we're processing
        for line in file:
            # Detect start of data sections for S2 to S31
            if line.strip() == "#------------------------------------------------------":
                # Toggle to next section (S2 to S31) after encountering each separator
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
                elif data_section == 'S7':
                    data_section = 'S8'
                elif data_section == 'S8':
                    data_section = 'S9'
                elif data_section == 'S9':
                    data_section = 'S10'
                elif data_section == 'S10':
                    data_section = 'S11'
                elif data_section == 'S11':
                    data_section = 'S12'
                elif data_section == 'S12':
                    data_section = 'S13'
                elif data_section == 'S13':
                    data_section = 'S14'
                elif data_section == 'S14':
                    data_section = 'S15'
                elif data_section == 'S15':
                    data_section = 'S16'
                elif data_section == 'S16':
                    data_section = 'S17'
                elif data_section == 'S17':
                    data_section = 'S18'
                elif data_section == 'S18':
                    data_section = 'S19'
                elif data_section == 'S19':
                    data_section = 'S20'
                elif data_section == 'S20':
                    data_section = 'S21'
                elif data_section == 'S21':
                    data_section = 'S22'
                elif data_section == 'S22':
                    data_section = 'S23'
                elif data_section == 'S23':
                    data_section = 'S24'
                elif data_section == 'S24':
                    data_section = 'S25'
                elif data_section == 'S25':
                    data_section = 'S26'
                elif data_section == 'S26':
                    data_section = 'S27'
                elif data_section == 'S27':
                    data_section = 'S28'
                elif data_section == 'S28':
                    data_section = 'S29'
                elif data_section == 'S29':
                    data_section = 'S30'
                elif data_section == 'S30':
                    data_section = 'S31'
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
                elif data_section == 'S8':
                    s8_mag = float(parts[1])  # S8 magnitude in dB
                    s8_magnitudes.append(s8_mag)
                elif data_section == 'S9':
                    s9_mag = float(parts[1])  # S9 magnitude in dB
                    s9_magnitudes.append(s9_mag)
                elif data_section == 'S10':
                    s10_mag = float(parts[1])  # S10 magnitude in dB
                    s10_magnitudes.append(s10_mag)
                elif data_section == 'S11':
                    s11_mag = float(parts[1])  # S11 magnitude in dB
                    s11_magnitudes.append(s11_mag)
                elif data_section == 'S12':
                    s12_mag = float(parts[1])  # S12 magnitude in dB
                    s12_magnitudes.append(s12_mag)
                elif data_section == 'S13':
                    s13_mag = float(parts[1])  # S13 magnitude in dB
                    s13_magnitudes.append(s13_mag)
                elif data_section == 'S14':
                    s14_mag = float(parts[1])  # S14 magnitude in dB
                    s14_magnitudes.append(s14_mag)
                elif data_section == 'S15':
                    s15_mag = float(parts[1])  # S15 magnitude in dB
                    s15_magnitudes.append(s15_mag)
                elif data_section == 'S16':
                    s16_mag = float(parts[1])  # S16 magnitude in dB
                    s16_magnitudes.append(s16_mag)
                elif data_section == 'S17':
                    s17_mag = float(parts[1])  # S17 magnitude in dB
                    s17_magnitudes.append(s17_mag)
                elif data_section == 'S18':
                    s18_mag = float(parts[1])  # S18 magnitude in dB
                    s18_magnitudes.append(s18_mag)
                elif data_section == 'S19':
                    s19_mag = float(parts[1])  # S19 magnitude in dB
                    s19_magnitudes.append(s19_mag)
                elif data_section == 'S20':
                    s20_mag = float(parts[1])  # S20 magnitude in dB
                    s20_magnitudes.append(s20_mag)
                elif data_section == 'S21':
                    s21_mag = float(parts[1])  # S21 magnitude in dB
                    s21_magnitudes.append(s21_mag)
                elif data_section == 'S22':
                    s22_mag = float(parts[1])  # S22 magnitude in dB
                    s22_magnitudes.append(s22_mag)
                elif data_section == 'S23':
                    s23_mag = float(parts[1])  # S23 magnitude in dB
                    s23_magnitudes.append(s23_mag)
                elif data_section == 'S24':
                    s24_mag = float(parts[1])  # S24 magnitude in dB
                    s24_magnitudes.append(s24_mag)
                elif data_section == 'S25':
                    s25_mag = float(parts[1])  # S25 magnitude in dB
                    s25_magnitudes.append(s25_mag)
                elif data_section == 'S26':
                    s26_mag = float(parts[1])  # S26 magnitude in dB
                    s26_magnitudes.append(s26_mag)
                elif data_section == 'S27':
                    s27_mag = float(parts[1])  # S27 magnitude in dB
                    s27_magnitudes.append(s27_mag)
                elif data_section == 'S28':
                    s28_mag = float(parts[1])  # S28 magnitude in dB
                    s28_magnitudes.append(s28_mag)
                elif data_section == 'S29':
                    s29_mag = float(parts[1])  # S29 magnitude in dB
                    s29_magnitudes.append(s29_mag)
                elif data_section == 'S30':
                    s30_mag = float(parts[1])  # S30 magnitude in dB
                    s30_magnitudes.append(s30_mag)
                elif data_section == 'S31':
                    s31_mag = float(parts[1])  # S31 magnitude in dB
                    s31_magnitudes.append(s31_mag)
    df9 = pd.DataFrame({'S9 Magnitude (dB)': s9_magnitudes})

    reshaped_data = pd.DataFrame(df9['S9 Magnitude (dB)'].values.reshape(1001, 23))
    # print(df9.size)
    # Optionally, rename the columns if needed
    reshaped_data.columns = [f'Column_{i + 1}' for i in range(23)]

    # Display the reshaped DataFrame
    # Column_1  Column_2  Column_3  Column_4  Column_5  Column_6  Column_7
    # print(reshaped_data)
    # Create a DataFrame from the lists
    # Create a DataFrame from the lists
    df = pd.DataFrame({
        'Frequency (GHz)': frequencies,
        'S2 Magnitude (dB)': s2_magnitudes,
        'S3 Magnitude (dB)': s3_magnitudes,
        'S4 Magnitude (dB)': s4_magnitudes,
        'S5 Magnitude (dB)': s5_magnitudes,
        'S6 Magnitude (dB)': s6_magnitudes,
        'S7 Magnitude (dB)': s7_magnitudes,
        'S8 Magnitude (dB)': s8_magnitudes,
        'S9 Magnitude (dB)': reshaped_data['Column_1'],
        'S10 Magnitude (dB)': reshaped_data['Column_2'],
        'S11 Magnitude (dB)': reshaped_data['Column_3'],
        'S12 Magnitude (dB)': reshaped_data['Column_4'],
        'S13 Magnitude (dB)': reshaped_data['Column_5'],
        'S14 Magnitude (dB)': reshaped_data['Column_6'],
        'S15 Magnitude (dB)': reshaped_data['Column_7'],
        'S16 Magnitude (dB)': reshaped_data['Column_8'],
        'S17 Magnitude (dB)': reshaped_data['Column_9'],
        'S18 Magnitude (dB)': reshaped_data['Column_10'],
        'S19 Magnitude (dB)': reshaped_data['Column_11'],
        'S20 Magnitude (dB)': reshaped_data['Column_12'],
        'S21 Magnitude (dB)': reshaped_data['Column_13'],
        'S22 Magnitude (dB)': reshaped_data['Column_14'],
        'S23 Magnitude (dB)': reshaped_data['Column_15'],
        'S24 Magnitude (dB)': reshaped_data['Column_16'],
        'S25 Magnitude (dB)': reshaped_data['Column_17'],
        'S26 Magnitude (dB)': reshaped_data['Column_18'],
        'S27 Magnitude (dB)': reshaped_data['Column_19'],
        'S28 Magnitude (dB)': reshaped_data['Column_20'],
        'S29 Magnitude (dB)': reshaped_data['Column_21'],
        'S30 Magnitude (dB)': reshaped_data['Column_22'],
        'S31 Magnitude (dB)': reshaped_data['Column_23']
    })

    # Add parameter values as columns in the DataFrame
    for param, value in param_values.items():
        df.insert(0, param, value)
    df.insert(0, 'C', 32)  # Insert 'C' as 32
    df.insert(0, 'R', 32)   # Insert 'R' as 4

    # Calculate the average of S2 to S31 and add it as a new column
    df['S Average'] = df.iloc[:, -30:].mean(axis=1)
    df.drop(df.columns[-31:-1], axis=1, inplace=True)

    # Optionally, save the DataFrame to a CSV file
    savePath = os.path.join(base_path, f"{i}.csv")
    df.to_csv(savePath, index=False)
