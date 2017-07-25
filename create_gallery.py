"""
"""

import matplotlib.pyplot as plt
import mpls
import json
import os
import shutil
import sys
import numpy as np

THUMB_FMT = '.png'


def sinplot(ax, flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        ax.plot(x, np.sin(x + i * .5) * (7 - i) * flip)


def main(stylelib, gallery):

    if not os.path.exists(stylelib):
        print('Specified stylelib does not exist')
        sys.exit(1)
    gallery_file = os.path.join(stylelib, 'gallery.json')
    if not os.path.exists(gallery_file):
        print('Could not find file gallery.json in specified stylelib')
        sys.exit(1)

    print('Cleaning up gallery ...')
    shutil.rmtree(gallery)
    os.makedirs(gallery)

    print('Collecting styles ...')
    entries = json.load(open(gallery_file))
    print('Generating thumbnails for {:d} styles ...'.format(len(entries)))

    for name, style in entries.items():
        fig_path = os.path.join(gallery, name+THUMB_FMT)
        with mpls.temp(**style):
            f = plt.figure()
            ax1 = f.add_subplot(111)
            # create plots
            sinplot(ax1)
            f.tight_layout()
            # save figure to gallery
            f.savefig(fig_path)

    print('Done')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('stylelib', type=str)
    parser.add_argument('gallery', type=str)
    args = parser.parse_args()
    main(args.stylelib, args.gallery)
