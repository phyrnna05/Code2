# Use the official Python image as a base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the image file and the script into the container
COPY image.jpg image.jpg          
# Ensure 'image.jpg' is in the same directory as the Dockerfile
COPY main.py main.py          

# Assuming the script is named 'script.py'

# Install OpenCV and necessary Python libraries
RUN pip install opencv-python-headless numpy

# Create the output directory (optional: ensures the folder exists)
RUN mkdir output_images

# Command to run the script
CMD ["python", "main.py"]
