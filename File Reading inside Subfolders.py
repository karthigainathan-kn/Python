import os
import pandas as pd

# Specify the root directory
root_directory = r'C:\Users\karthigainathan.muru\Desktop\SQL_Learn'

# Initialize a list to store file details
file_details = []

# Walk through the directory structure
for dirpath, _, filenames in os.walk(root_directory):
    for file in filenames:
        # Capture the full path and file name
        full_path = os.path.join(dirpath, file)
        file_details.append({'Folder Path': dirpath, 'File Name': file, 'Full Path': full_path})

# Create a Pandas DataFrame
df = pd.DataFrame(file_details)


# Specify the output CSV file path
output_csv_path = r'C:\Users\karthigainathan.muru\Desktop\all_file_details.csv'

# Save the DataFrame to a CSV file
df.to_csv(output_csv_path, index=False)

print(f"File details saved to {output_csv_path}")
