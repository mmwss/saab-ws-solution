from PIL import Image
import os

def fragment_image(image_path, output_dir, grid_size=(2, 2)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    img = Image.open(image_path)
    img_width, img_height = img.size
    rows, cols = grid_size
    fragment_width = img_width // cols
    fragment_height = img_height // rows

    fragment_number = 1
    for row in range(rows):
        for col in range(cols):
            left = col * fragment_width
            upper = row * fragment_height
            right = (col + 1) * fragment_width
            lower = (row + 1) * fragment_height

            fragment = img.crop((left, upper, right, lower))
            fragment_filename = f'fragment{fragment_number}.png'
            fragment.save(os.path.join(output_dir, fragment_filename))
            fragment_number += 1

if __name__ == '__main__':
    fragment_image('./data/fragments/6/_.jpg', './data/fragments/6', grid_size=(22, 23))
