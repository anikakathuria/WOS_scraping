# Title: search.py
# Date: Summer 2024
# Author: Anika Kathuria (ak4748@columbia.edu)

import os
import sys
import pandas as pd

# Check if the folder path is provided as a command line argument
if len(sys.argv) != 3:
    print("Usage: python3 search.py <folder_path> <search_term>")
    sys.exit(1)

# Get the folder path and search term from the command line arguments
folder_path = sys.argv[1]
search_term = sys.argv[2]

# List to store results
results = []

# Function to search for the term in each Excel file
def search_in_excel(file_path, search_term):
    try:
        # Load the Excel file
        xls = pd.ExcelFile(file_path)
        # Iterate through each sheet in the Excel file
        for sheet_name in xls.sheet_names:
            # Read the sheet into a DataFrame
            df = pd.read_excel(xls, sheet_name=sheet_name, dtype=str)
            # Check if the search term is in any cell
            if df.applymap(lambda x: search_term in str(x)).any().any():
                results.append((file_path, sheet_name))
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

# Iterate through all files in the subdirectories
for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith(".xlsx") or file_name.endswith(".xls"):
            file_path = os.path.join(root, file_name)
            search_in_excel(file_path, search_term)

# Convert results to a DataFrame and display
results_df = pd.DataFrame(results, columns=["File", "Sheet"])
print(results_df)

