# Title: consolidate_files.py
# Date: Summer 2024
# Author: Anika Kathuria (ak4748@columbia.edu)

import pandas as pd
import os
import sys

def consolidate_excel_files(root_folder, output_file):
    # List to hold dataframes
    all_dataframes = []

    # Walk through the root folder
    for subdir, _, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.xls'):
                file_path = os.path.join(subdir, file)
                # Read each excel file
                df = pd.read_excel(file_path)
                all_dataframes.append(df)

    # Concatenate all dataframes
    combined_df = pd.concat(all_dataframes, ignore_index=True)

    # Drop duplicate rows
    combined_df.drop_duplicates(inplace=True)

    # Save the consolidated dataframe to an excel file
    combined_df.to_excel(output_file, index=False)

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python3 consolidate_files.py <root_folder> <output_file>")
        sys.exit(1)

    # Get the command line arguments
    root_folder = sys.argv[1]
    output_file = sys.argv[2]

    # Run the consolidation function
    consolidate_excel_files(root_folder, output_file)

