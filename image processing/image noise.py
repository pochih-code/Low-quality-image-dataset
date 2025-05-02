import numpy as np
import cv2
import os

input_folder = <image_input_path>  # Replace with the path to your input folder
output_folder = <image_output_path>  # Replace with the path to your output folder
os.makedirs(output_folder, exist_ok=True)

# Check if the file is an image (you can add more formats if needed)
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        if image is not None:
            mean = <> # Replace with the desired mean value for Gaussian noise
            std = <> # Replace with the desired standard deviation for Gaussian noise
            noise = np.random.normal(mean, std, image.shape).astype(np.float32)
            noisy_image = image.astype(np.float32) + noise
            noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, noisy_image)
