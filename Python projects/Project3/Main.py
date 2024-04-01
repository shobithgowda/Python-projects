import os  # Import the os module for file operations
import cv2  # Import the OpenCV library for image processing

# Function to resize an image
def resize_image(input_path, output_path, width=None, height=None, quality=95):
    # Read the image from the input path
    image = cv2.imread(input_path)

    # Check if the image is loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return

    # Calculate new dimensions while preserving aspect ratio
    if width is None and height is None:
        print("Error: Please provide either width or height for resizing.")
        return

    if width is None:
        aspect_ratio = height / float(image.shape[0])
        new_width = int(image.shape[1] * aspect_ratio)
        new_height = height
    elif height is None:
        aspect_ratio = width / float(image.shape[1])
        new_width = width
        new_height = int(image.shape[0] * aspect_ratio)
    else:
        new_width = width
        new_height = height

    # Resize the image using the calculated dimensions
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

    # Save the resized image to the output path
    cv2.imwrite(output_path, resized_image, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

    print("Image resized successfully.")

# Main function
def main():
    # Get input and output paths from the user
    input_path = input("Enter the path of the original image: ")
    output_path = input("Enter the path to save the resized image: ")

    # Get resizing options from the user
    width = input("Enter the width of the resized image (press Enter to keep aspect ratio): ")
    height = input("Enter the height of the resized image (press Enter to keep aspect ratio): ")
    quality = input("Enter the quality of the resized image (0-100, default is 95): ")

    # Convert user inputs to appropriate data types
    width = int(width) if width else None
    height = int(height) if height else None
    quality = int(quality) if quality else 95

    # Resize the image using the provided parameters
    resize_image(input_path, output_path, width, height, quality)

if __name__ == "__main__":
    main()  # Call the main function if the script is executed directly
