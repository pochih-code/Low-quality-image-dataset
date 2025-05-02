import os
from PIL import Image

# Set the desired quality for lossy compression (1-100)
Quality = <> 

def compress_image_lossy(input_path, output_path, quality=Quality):
    img = Image.open(input_path)
    img.save(output_path, format='JPEG', quality=quality, optimize=True)

# Check if the file is an image (you can add more formats if needed)
def compress_images_in_folder(input_folder, output_folder, quality=Quality):
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_file_path = os.path.join(input_folder, filename)
            output_file_name = os.path.splitext(filename)[0] + ".jpg"
            output_file_path = os.path.join(output_folder, output_file_name)
            compress_image_lossy(input_file_path, output_file_path, quality)

input_folder = <image_input_path>  # Replace with the path to your input folder
output_folder = <image_output_path>  # Replace with the path to your output folder
compress_images_in_folder(input_folder, output_folder)
