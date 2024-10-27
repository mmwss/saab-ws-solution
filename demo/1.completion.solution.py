from PIL import Image, ImageDraw, ImageFont

def apply_watermark(input_image_path, output_image_path, watermark_text):
    # Open the original image
    original = Image.open(input_image_path).convert("RGBA")
    
    # Make a blank image for the watermark with the same size
    watermark = Image.new("RGBA", original.size)
    draw = ImageDraw.Draw(watermark)
    
    # Choose a font and size
    font = ImageFont.load_default()
    
    # Get the width and height of the text to be added
    text_width, text_height = draw.textsize(watermark_text, font)
    
    # Calculate the position at the bottom right
    width, height = original.size
    x = width - text_width - 10
    y = height - text_height - 10
    
    # Add text to the watermark image
    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))
    
    # Combine the original image with the watermark
    combined = Image.alpha_composite(original, watermark)
    
    # Save the result
    combined.convert("RGB").save(output_image_path, "JPEG")
    
# Example usage
apply_watermark('input.jpg', 'output.jpg', '© YourName')
