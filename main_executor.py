# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:58:58 2024

@author: kevin
"""
import main  # Assuming main.py has a callable function, e.g., main()
import main2  # Assuming main2.py has a callable function, e.g., main()

def main_executor():
    while True:
        print("\nWelcome to the analysis of your dilution series!")
        print("1. Analyze your pictures and turn them into a CSV dataset.")
        print("2. Combine and plot your data.")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == '1':
            print("Ok lets analyse some pictures...")
            main.picture_box_anal()  # Call the main function from main.py
        elif choice == '2':
            print("Ok lets plot some nice grapes...")
            main2.process_and_plot_data()  # Call the main function from main2.py
        elif choice == '3':
            print("you finish? Goodbye!")
            break  # Exit the loop, thereby ending the program
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_executor()


