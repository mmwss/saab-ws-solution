import os

def get_fragments_list(directory):
    files = os.listdir(directory)

    fragments = [os.path.join(directory, f) for f in files if f.endswith('.png')]

    # sort fragments by number in filename
    fragments.sort(key=lambda x: int(x.split('fragment')[-1].split('.')[0]))

    return fragments
