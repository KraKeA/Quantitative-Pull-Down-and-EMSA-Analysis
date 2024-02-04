# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 23:47:52 2024

@author: kevin
"""
import os

def get_user_input():
    while True:
        file_name = input("Enter the full name of the picture to analyze: ")
        # Check if file exists in the folder
        if not os.path.exists(os.path.join('images_to_analyse', file_name)):
            print("File not found in the images_to_analyse folder. Please try again.")
            continue
        else:
            break

    while True:
        try:
            cut_off_threshold = int(input("Enter value for cut off threshold (0 to 250): "))
            # Check if cut_off_threshold is between 0 and 250
            if 0 <= cut_off_threshold <= 250:
                break
            else:
                print("Value must be between 0 and 250. Please try again.")
        except ValueError:
            print("Please enter a valid number. Please try again.")

    while True:
        limit = input("Do you want to use '<' or '>' for cut off threshold? Enter '<' or '>': ")
        # Check if limit is '<' or '>'
        if limit in ['<', '>']:
            break
        else:
            print("Invalid input. Please enter '<' or '>'.")

    init_value = input("Enter the highest concentration of your dilution series in microMolar: ")
    lanes = int(input("Enter how many lanes you are analysing in the picture: "))

    return file_name, cut_off_threshold, limit, init_value, lanes

