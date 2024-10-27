"""
An image has accidentally been shredded into 506 fragments.
The fragments have been saved in the data/fragments directory.
The fragments are named fragment1.png, fragment2.png, ..., fragment506.png.
From what we know the image was shredded into a 22x23 grid.
It would be easy to restore the image but
the code was written by a junior developer who left the company
and a lot of bugs. Restore the image.
"""

GROUP_NUMBER = 1 # Change this to your group number
# To test this challenge, only run this file (main.py).
# DO NO MODIFY ANYTHING BEYOND THIS POINT

import pretty_errors
from processor import ImageAssembler
from utils import get_fragments_list

def main():
    fragments_directory = f'./data/fragments/{GROUP_NUMBER}'
    fragments = get_fragments_list(fragments_directory)

    assembler = ImageAssembler(fragments)
    assembler.assemble_image((22, 23))
    assembler.save('restored_image.png')

if __name__ == '__main__':
    main()
