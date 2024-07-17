# Title: generate_queries.py
# Date: Summer 2024
# Author: Anika Kathuria (ak4748@columbia.edu)

import pandas as pd
import sys

def process_excel_to_text(excel_file, sheet_name, column_name, output_file):
    try:
        # Load the Excel file with header in row 4 (index 3)
        df = pd.read_excel(excel_file, sheet_name=sheet_name, header=3)
        
        # Extract the specified column and drop NA values
        column_data = df[column_name].dropna().astype(str)
        
        # Group the column data into chunks of 49
        chunk_size = 49
        chunks = [column_data[i:i + chunk_size] for i in range(0, len(column_data), chunk_size)]
        
        with open(output_file, 'w') as file:
            for i, chunk in enumerate(chunks):
                line = ' OR '.join([f'"{item}"' for item in chunk])
                file.write(line + '\n')
                print(f"Written chunk {i + 1}")
        
        print(f"Output written to {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 generate_queries.py <excel_file> <sheet_name> <column_name> <output_file>")
    else:
        excel_file = sys.argv[1]
        sheet_name = sys.argv[2]
        column_name = sys.argv[3]
        output_file = sys.argv[4]
        process_excel_to_text(excel_file, sheet_name, column_name, output_file)

