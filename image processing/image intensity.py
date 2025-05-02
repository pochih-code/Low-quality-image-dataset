import cv2
import numpy as np
import os
import glob

input_folder = <image_input_path>  # Replace with the path to your input folder
output_folder = <image_output_path>  # Replace with the path to your output folder
gamma_value = <>  # Replace with the desired gamma value

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Check if the file is an image (you can add more formats if needed) 
image_extensions = ['*.jpg', '*.jpeg', '*.png']
image_paths = []
for ext in image_extensions:
    image_paths.extend(glob.glob(os.path.join(input_folder, ext)))

invGamma = 1.0 / gamma_value
table = np.array([((i / 255.0) ** invGamma) * 255 for i in range(256)]).astype("uint8")

for img_path in image_paths:
    img = cv2.imread(img_path)
    corrected_img = cv2.LUT(img, table)
    filename = os.path.basename(img_path)
    output_path = os.path.join(output_folder, filename)
    cv2.imwrite(output_path, corrected_img)
