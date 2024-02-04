# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 20:12:48 2024

@author: kevin
"""
# This is image_data_analysis/data_processing.py

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def model(x, a, b, Kd, active_fraction):
    return (a * ((active_fraction*x) / ((active_fraction*x) + Kd))) + b

def fit_model_and_plot(dataframe, plot_folder, use_log_scale=False, plot_title="Quantitative Pulldown Assay", active_fraction=1):
    x_data = dataframe['Concentration(yM)']
    y_data = dataframe['Mean']

    # Wrapper function to include active_fraction in the model
    def model_wrapper(x, a, b, Kd):
        return model(x, a, b, Kd, active_fraction)

    initial_a = y_data.max()
    initial_b = y_data.min()

    params, _ = curve_fit(model_wrapper, x_data, y_data, p0=[initial_a, initial_b, 1.0])

    print(f"Optimized parameters: a={params[0]}, b={params[1]}, Kd={params[2]}")

    plt.figure()
    x_fit = np.logspace(np.log10(x_data.min()), np.log10(x_data.max()), 1000)
    y_fit = model(x_fit, *params, active_fraction)
    plt.plot(x_fit, y_fit, 'r--', color='green', linewidth=1, label=f"Fit Kd:{params[2]:.2f}$\mu$M")
    plt.errorbar(dataframe['Concentration(yM)'], dataframe['Mean'], yerr=dataframe['stdev'], fmt='none', ecolor='#6e0202', elinewidth=1, capsize=2, label='one standard deviation')
    plt.scatter(dataframe['Concentration(yM)'], dataframe['Mean'], color='black', label="intensity")

    xlabel = "Free ligand concentration"
    if use_log_scale:
        plt.xscale('log')
        xlabel += " Log[$\mu$M]"
    else:
        xlabel += " [$\mu$M]"
    plt.xlabel(xlabel)

    plt.ylabel("Normalized Signal Intensity")
    plt.title(plot_title)
    plt.legend(loc='lower right', fontsize=8)
    plt.grid(True)
    plt.savefig(f'{plot_folder}/{plot_title}.png', dpi=300)
    print(f"{plot_title}.png has ben saved in {plot_folder}")
    plt.show()

