# mpls -- a lightweight manager and library of matplotlib plotting styles

This is a small lightweight Python package that manages a repository of
matplotlib styles and makes it easy to create, edit, and use different styles.

## Styles

mpls styles are organized into three categories: context, style, and
palette.

The *context* defines size relevant properties such as figure size, size of marker
points, etc.

The *style* defines the general style properties such as ...

The *palette* defines the color properties such as the colormap of images or the
color of markers and lines.

## Categories

A list of scientific journal name abbreviations can be found here:
     https://images.webofknowledge.com/images/help/WOS/A_abrvjt.html

## Examples

```python

import matplotlib.pyplot as plt
import mpls

mpls.use('a4', 'thesis')

# create some plot
...

with mpls.context('a4-landscape', 'thesis', type='context'):
   # temporarily switch to A4 landscape format
   ...

# continue with regular A4 format
...
```
