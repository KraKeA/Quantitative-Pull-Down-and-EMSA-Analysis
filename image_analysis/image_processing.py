# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 23:49:39 2024

@author: kevin
"""
import cv2

def load_and_scale_image(file_name):
    image = cv2.imread(file_name)
    window_width, window_height = 800, 600
    scale_x, scale_y = window_width / image.shape[1], window_height / image.shape[0]
    scale = min(scale_x, scale_y)
    scaled_width, scaled_height = int(image.shape[1] * scale), int(image.shape[0] * scale)
    scaled_image = cv2.resize(image, (scaled_width, scaled_height))
    return scaled_image, scale, image

def draw_boxes(scaled_image, scale, lines_total):
    box_coordinates = []
    current_box = None

    def draw_box(event, x, y, flags, param):
        nonlocal current_box
        if event == cv2.EVENT_LBUTTONDOWN:
            # Start a new box
            current_box = [x / scale, y / scale, x / scale, y / scale]
            box_coordinates.append(current_box)
        elif event == cv2.EVENT_MOUSEMOVE and current_box is not None:
            # Update the current box dimensions
            current_box[2] = x / scale
            current_box[3] = y / scale
        elif event == cv2.EVENT_LBUTTONUP:
            # Finalize the current box
            current_box[2] = x / scale
            current_box[3] = y / scale
            current_box = None

    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Image", scaled_image.shape[1], scaled_image.shape[0])
    cv2.setMouseCallback("Image", draw_box)

    while True:
        clone = scaled_image.copy()
        for box in box_coordinates:
            cv2.rectangle(clone, (int(box[0] * scale), int(box[1] * scale)), 
                          (int(box[2] * scale), int(box[3] * scale)), (0, 255, 0), 2)
        cv2.imshow("Image", clone)
        key = cv2.waitKey(1) & 0xFF
        if key == 27 or len(box_coordinates) == lines_total:  # Exit on ESC or when required boxes are drawn
            break
    cv2.destroyAllWindows()
    return box_coordinates
