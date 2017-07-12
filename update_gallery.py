"""
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import mpls
import json
import os
import shutil
import numpy as np

here = os.path.abspath(os.path.dirname(__file__))
stylelib = os.path.join(here, 'stylelib')
gallery = os.path.join(here, 'gallery')
data_url = os.path.join(stylelib, '{category}/{name}.{type}.json')


def sinplot(ax, flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        ax.plot(x, np.sin(x + i * .5) * (7 - i) * flip)


def main():

    print('Cleaning up gallery ...')
    shutil.rmtree(gallery)
    os.mkdir(gallery)

    print('Collecting styles ...')
    entries = mpls.utils.all_styles(stylelib)
    print('Generating thumbnails for {0:d} styles ...'.format(len(entries)))

    for category, name in entries:
        # create category folders if necessary
        cat_dir = os.path.join(gallery, category)
        if not os.path.exists(cat_dir):
            os.mkdir(cat_dir)

        fig_path = os.path.join(here, 'gallery', category, '{}.{}'.format(name, mpls.config.THUMB_FMT))

        with mpls.context(name, category, data_url=data_url):
            f = plt.figure()
            ax1 = f.add_subplot(111)
            # create plots
            sinplot(ax1)
            f.tight_layout()
            # save figure to gallery
            f.savefig(fig_path)

    print('Done')


if __name__ == '__main__':
    main()
