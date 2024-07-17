# Title: reorganize_columns.py
# Date: Summer 2024
# Author: Anika Kathuria (ak4748@columbia.edu)


import pandas as pd
import sys

def reorganize_columns(input_file, output_file):
    # Read the input excel file
    df = pd.read_excel(input_file)

    # Define the new column order and names
    column_mapping = {
        'Funding Name Preferred': 'Funder',
        'DOI': 'Specific Study DOI',
        'DOI Link': 'Source',
        'Publication Year': 'Year'
    }

    # New columns to be added at the beginning and should be empty
    new_columns = [
        'Donation Amount',
        'Type of Donations: (gift, sponsored projects...)',
        'Columbia school',
        'Columbia Affiliates',
        'Which Specific Columbia Program?',
        'Notes'
    ]

    # Columns to be added at the end
    additional_columns = [
        'Author Full Names',
        'Article Title',
        'Source Title',
        'Affiliations',
        'Funding Text',
        'ISSN'
    ]

    # Rename the columns based on the mapping
    df.rename(columns=column_mapping, inplace=True)

    # Add new empty columns
    for col in new_columns:
        df[col] = ""

    # Create the output DataFrame with the reordered columns
    output_df = df[
        [
            'Funder',
            'Donation Amount',
            'Year',
            'Type of Donations: (gift, sponsored projects...)',
            'Columbia school',
            'Columbia Affiliates',
            'Which Specific Columbia Program?',
            'Source',
            'Specific Study DOI',
            'Notes'
        ] + additional_columns
    ]

    # Save the reorganized DataFrame to the output Excel file
    output_df.to_excel(output_file, index=False)

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python3 reorganize_columns.py <input_file> <output_file>")
        sys.exit(1)

    # Get the command line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Run the reorganization function
    reorganize_columns(input_file, output_file)

