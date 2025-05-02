import cv2
import os

input_folder = <image_input_path>  # Replace with the path to your input folder
output_folder = <image_output_path>  # Replace with the path to your output folder

os.makedirs(output_folder, exist_ok=True)

# You can adjust this value as needed
kernel_size = (5, 5)  # Size of the kernel for blurring

for filename in os.listdir(input_folder):
    img_path = os.path.join(input_folder, filename)
    
    # Check if the file is an image (you can add more formats if needed)
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        image = cv2.imread(img_path)

        blurred_image = cv2.blur(image, kernel_size)

        output_path = os.path.join(output_folder, filename)
        success = cv2.imwrite(output_path, blurred_image)
