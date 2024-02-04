# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 23:46:10 2024

@author: kevin
"""
import os
from image_analysis import get_user_input, load_and_scale_image, draw_boxes, analyze_boxes, create_data_frame

def picture_box_anal():
    base_file_name, cut_off_threshold, limit, init_value, lanes = get_user_input()
    
    # Construct the path to the image file
    file_path = os.path.join('images_to_analyse', base_file_name)
    
    scaled_image, scale, original_image = load_and_scale_image(file_path)
    box_coordinates = draw_boxes(scaled_image, scale, lanes * 2 + 1)
    results = analyze_boxes(original_image, box_coordinates, cut_off_threshold, limit, init_value, lanes)
    result_df = create_data_frame(results, init_value, lanes)
    
    # Modify the base_file_name for the result_csv
    modified_name = base_file_name.split('.')[0]  # Remove extension and extra characters
    result_csv_path = os.path.join('image_analysis_results', modified_name + '.csv')
    
    # Ensure the results directory exists
    os.makedirs('image_analysis_results', exist_ok=True)
    
    result_df.to_csv(result_csv_path, index=False)
    print("Analysis complete. Results saved to:", result_csv_path)

if __name__ == "__main__":
    picture_box_anal() 

