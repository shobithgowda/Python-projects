import streamlit as st  # Import Streamlit library
import numpy as np  # Import NumPy library
from PIL import Image  # Import PIL (Python Imaging Library) for image processing

# Function to resize the image
def resize_image(image, new_size):
    resized_image = image.resize(new_size)  # Resize the image to the new size
    return resized_image

# Main function to create the Streamlit app
def main():
    st.title("Image Resizer")  # Set the title of the app

    # Allow users to upload an image file (JPEG or PNG)
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:  # Check if an image is uploaded
        # Read the uploaded image file
        image = Image.open(uploaded_file)

        # Display the original image with caption
        st.image(image, caption="Original Image", use_column_width=True)

        # Prompt users to input new width and height for resizing
        new_width = st.number_input("Enter new width:", min_value=1)
        new_height = st.number_input("Enter new height:", min_value=1)

        if st.button("Resize"):  # Check if the "Resize" button is clicked
            new_size = (new_width, new_height)  # Create a tuple for new size
            resized_image = resize_image(image, new_size)  # Resize the image

            # Display the resized image with caption
            st.image(resized_image, caption=f"Resized Image ({new_width}x{new_height})", use_column_width=True)

if __name__ == "__main__":
    main()  # Call the main function to run the Streamlit app
