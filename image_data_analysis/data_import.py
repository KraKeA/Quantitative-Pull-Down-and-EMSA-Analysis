# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 20:10:10 2024

@author: kevin
"""

import pandas as pd
import glob

def import_text_files(file_pattern):
    file_list = glob.glob(file_pattern)
    dfs = []
    for file in file_list:
        df = pd.read_csv(file, sep=',')
        df['Filename'] = file
        dfs.append(df)
    if dfs:
        return pd.concat(dfs, ignore_index=True)
    else:
        return None

def combine_dataframes(dataframes):
    combined_df = pd.DataFrame()
    # Add 'Concentration(yM)' at the beginning
    combined_df['Concentration(yM)'] = dataframes[0]['Concentration']
    combined_df['Sample'] = range(1, 11)  # Assuming there are 10 samples

    for i, df in enumerate(dataframes, start=1):
        combined_df[f'NormalizedSample_{i}'] = df['NormalizedSample']


    num_samples = len(dataframes)  # Number of dataframes equals number of samples
    combined_df['Mean'] = combined_df.iloc[:, 2:2+num_samples].mean(axis=1)
    combined_df['stdev'] = combined_df.iloc[:, 2:2+num_samples].std(axis=1)

    print(combined_df)
    return combined_df

