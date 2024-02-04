# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 23:51:55 2024

@author: kevin
"""
import numpy as np
import pandas as pd

def analyze_boxes(image, box_coordinates, cut_off_threshold, limit, init_value, lanes):
    results = []
    for box in box_coordinates:
        x1, y1, x2, y2 = map(int, box)
        roi = image[y1:y2, x1:x2]
        if limit == '<':
            surface_area = np.sum(roi < cut_off_threshold)
        elif limit == '>':
            surface_area = np.sum(roi > cut_off_threshold)
        else:
            raise ValueError("Invalid limit value. Please enter '<' or '>'.")
        results.append(surface_area)
    return results

def create_data_frame(results, init_value, lanes):
    df = pd.DataFrame({
        "Box": [f"Box {i + 1}" for i in range(len(results))],
        "SurfaceArea": results
    })
    return df
