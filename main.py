import cv2
import os

# Define the input image file name
input_image_file = 'image.jpg'  # Change this to your image file name

# Read the image using OpenCV
image = cv2.imread(input_image_file)

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not read the image.")
    exit()

# Get the dimensions of the image
height, width = image.shape[:2]

# Calculate the center of the image
center_x, center_y = width // 2, height // 2

# Split the image into four quadrants
quadrants = {
    "top_left": image[0:center_y, 0:center_x],
    "top_right": image[0:center_y, center_x:width],
    "bottom_left": image[center_y:height, 0:center_x],
    "bottom_right": image[center_y:height, center_x:width],
}

# Create an output directory if it doesn't exist
output_dir = 'output_images'
os.makedirs(output_dir, exist_ok=True)

# Save each quadrant as a separate image
for name, quadrant in quadrants.items():
    cv2.imwrite(os.path.join(output_dir, f'{name}.jpg'), quadrant)

# Perform edge detection using Canny
edges = cv2.Canny(image, 100, 200)

# Save the edge detection image
cv2.imwrite(os.path.join(output_dir, 'edges.jpg'), edges)

print("Images saved in the 'output_images' directory.")
