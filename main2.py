# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 00:53:15 2024

@author: kevin
"""
import os
from image_data_analysis import import_text_files, combine_dataframes, fit_model_and_plot, select_csv_files

def process_and_plot_data(plot_title=None, active_fraction=None, use_log_scale=None):
    # Ensure the folders 'temp_results' and 'Result_plot' exist
    os.makedirs('temp_results', exist_ok=True)
    os.makedirs('Result_plot', exist_ok=True)

    file_patterns = select_csv_files()

    dataframes = [import_text_files(pattern) for pattern in file_patterns]

    combined_df = combine_dataframes(dataframes)

    # Save the combined DataFrame in the 'temp_results' folder
    combined_df.to_csv('temp_results/combineddfforplot.csv', index=False)

    # Collect user inputs if not provided
    if plot_title is None:
        plot_title = input("Enter the title for the plot: ")
    if active_fraction is None:
        active_fraction = float(input("Enter the percentage of the ligand that is active (0-100): ")) / 100
    if use_log_scale is None:
        use_log_scale = input("Would you like to use a logarithmic scale on the x-axis? (yes/no): ").strip().lower() == 'yes'

    # Plotting
    fit_model_and_plot(combined_df, 'Result_plot', use_log_scale, plot_title, active_fraction)

    # Delete the 'combineddfforplot.csv' file
    file_path = 'temp_results/combineddfforplot.csv'
    if os.path.exists(file_path):
        os.remove(file_path)
        print("The file combineddfforplot.csv has been deleted.")
    else:
        print("The file combineddfforplot.csv does not exist.")
    
    print("All finished :D")

if __name__ == "__main__":
    process_and_plot_data()
