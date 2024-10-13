import pandas as pd
import glob
import os

# Define the directory containing the CSV files
directory = r'D:\Intrusion detection system\IDS dataset'  # Change to the correct path of your dataset folder

# Use glob to find all CSV files in the directory
csv_files = glob.glob(os.path.join(directory, "*.csv"))

# Create an empty list to hold the dataframes
df_list = []

# Loop through the CSV files and append each to the list
for file in csv_files:
    print(file)
    df = pd.read_csv(file)
    #df_list.append(df)

# Concatenate all dataframes into one
combined_df = pd.concat(df_list, axis=1, ignore_index=True)

# Save the combined dataframe to a new CSV file
combined_df.to_csv('D:\Intrusion detection system\IDS dataset\combined_ids_dataset.csv', index=False)

print("All CSV files have been successfully combined into 'combined_ids_dataset.csv'.")
