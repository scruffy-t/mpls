"""
"""

import matplotlib.pyplot as plt
import seaborn as sns
import inshore
import json
import os
import numpy as np

from os import path

here = path.abspath(path.dirname(__file__))

THUMB_FMT = 'png'


def find_all(type):
    entries = []
    for category in os.scandir(path.join(here, type)):
        if category.is_dir():
            for name in os.scandir(path.join(here, type, category.path)):
                if name.is_file() and name.path.endswith('.json'):
                    entries.append((path.basename(category.path), path.basename(name.path)))
    return entries


def get_local(category, name):
    settings = inshore.DEFAULT_SETTINGS.copy()
    for type in ('context', 'style', 'palette'):
        fp = os.path.join(here, type, category, name)
        if path.exists(fp):
            with open(fp, 'r') as f:
                s = inshore.utils.remove_comments(f.read())
                try:
                    settings[type] = json.loads(s)
                except json.JSONDecodeError as e:
                    print('Invalid {} file {}/{} [{}:{}]:\n {}'.format(type, category, name, e.lineno, e.colno, e.msg))
    return settings


def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)


def main():
    # collect inshore context, palette, and styles
    entries = set(find_all('context')+find_all('style')+find_all('palette'))
    print('Found {:d} entries'.format(len(entries)))

    for category, name in entries:
        # temporarily apply custom style
        s = get_local(category, name)
        sns.set(**s)
        # create plot
        sinplot()
        # set figure title
        name = name.replace('.json', '')
        full_name = '{0}/{1}'.format(category, name)

        thumb = """
        {0}
        context: {1}, style: {2}, palette: {3}
        """

        fallback = inshore.DEFAULT_SETTINGS

        context = full_name if isinstance(s['context'], dict) else '(default)'
        style = full_name if isinstance(s['style'], dict) else '(default)'
        palette = full_name if isinstance(s['palette'], dict) else '(default)'
        desc = thumb.format(full_name, context, style, palette)
        fig_path = path.join(here, 'gallery', '{0}_{1}.{2}'.format(category, name, THUMB_FMT))

        plt.title(desc)
        # plt.tight_layout()
        # save figure to ./gallery
        plt.savefig(fig_path)


if __name__ == '__main__':
    main()
