"""
You are tasked with writing a Python script that:

- Loads a local image from disk.
- Applies a semi-transparent text watermark to the image.
- Saves the watermarked image to disk.
"""

from PIL import Image, ImageDraw, ImageFont

def apply_watermark(input_image_path, output_image_path, watermark_text):
    # Open the original image
    original = Image.open(input_image_path).convert("RGBA")
    
    # Make a blank image for the watermark with the same size
    # Use AI code completion here to create the watermark image
    
    # Combine the original image with the watermark
    # Use AI code completion here to combine images
    
    # Save the result
    # Use AI code completion here to save the image
    pass  # Remove this pass statement after adding your code

# Example usage
apply_watermark('input.jpg', 'output.jpg', '© YourName')
