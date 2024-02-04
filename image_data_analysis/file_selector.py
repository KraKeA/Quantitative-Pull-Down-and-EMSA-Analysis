# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 00:57:42 2024

@author: kevin
"""
import os

def select_csv_files():
    # Define the directory containing the CSV files
    directory_path = 'image_analysis_results'
    
    # Initialize a list to store the selected file paths
    file_patterns = []
    
    while True:
        # Prompt the user for the file name
        filename = input("Enter the name of the CSV file (with or without '.csv'): ").strip()
        
        # Append '.csv' if not already present
        if not filename.endswith('.csv'):
            filename += '.csv'
        
        # Construct the full file path
        full_path = os.path.join(directory_path, filename)
        
        # Check if the file exists
        if os.path.exists(full_path):
            file_patterns.append(full_path)
            print(f"File '{filename}' has been added.")
        else:
            print(f"File '{filename}' does not exist in the directory '{directory_path}'. Please try again.")
        
        # Ask the user if they want to add another file
        add_another = input("Would you like to add another file? (yes/no): ").lower()
        if add_another != 'yes':
            break
    
    # Summarize the selected files
    if file_patterns:
        print("\nFiles selected for evaluation:")
        for file in file_patterns:
            print(f"'{file}',")
    else:
        print("No files were selected.")
    print(file_patterns)
    return file_patterns


