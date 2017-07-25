# mpls
`mpls` is a small lightweight Python package that manages a repository of
matplotlib styles and makes it easy to create, edit, and use different styles.

Please, refer to the respective [matplotlib page][3] for more information on how to customize the style of your
plots directly with matplotlib.

## About
Similar to [seaborn][1], `mpls` styles are organized in three types: **context**, **style**, and
**palette**.

The **context** defines size relevant properties such as figure size, size of marker
points, etc.
More details on which `rcParams` belong to the **context** can be found [here](doc/context.md).

The **style** defines the general style properties such as basic figure _colors_ and _fonts_.
More details on which `rcParams` belong to the **style** can be found [here](doc/style.md). 

The **palette** defines the color properties such as the colormap of images or the
color of markers and lines.
More details on which `rcParams` belong to the **palette** can be found [here](doc/palette.md).

### Style files
Technically, each of the three style types represents a subset of the `rcParams` dict in [matplotlib][2] and
parameters are stored in a dict in so-called _style files_. These style files are regular _json_ files, with the exception that
it is allowed to have C-style comments in the file. A small example of a valid **context** style file is
```javascript
{
    // this is a line comment
    "figure.figsize": [3, 4],
    
    /* this is a multi-
       line comment */
    "font.size": 10
}
```

_Note_: In the current version, parameters defined in style files are not restricted to a certain subset of `rcParams`.
Generally, you can define any parameter in any style file! This is useful in some cases. However, this may change in
the future and in order to make working with style files easy and intuitive, please restrict yourself to the
parameters specified in the respective style file documentation.

## Installation
The easiest way to install mpls is to use `pip`, i.e.
```
pip install mpls
```

However, if you want to work with the most recent version of `mpls`, you can just clone the repository and run setuptools in
the folder like 
```
python setup.py install
```

## Requirements
There is only one requirement
- `matplotlib`

obviously ...

## Examples
An example where the plotting context is modified temporarily.
```python
import matplotlib.pyplot as plt
import mpls

mpls.use(context='a4', style='thesis', palette='grayscale')

# create some plot
...

with mpls.temp(context='a4-landscape'):
   # temporarily switch to A4 landscape format
   ...

# continue with regular A4 format
...
```

An example of mixing `matplotlib` and `mpls` styles
```python
import matplotlib.pyplot as plt
import mpls

# mix a matplotlib style with an mpls palette
mpls.use('dark_background', palette='grayscale')

# create some plots
...
```

## Contributing
Contributions to the `mpls` code or the stylelib in this repository are very welcome. Just issue a pull request at the github page.

## Using a custom style library
As default `mpls` fetches styles from the stylelib folder in this repository. But it is also possible to fetch files from
any other _remote_ or _local_ repository. The easiest way to fetch `mpls` styles from a custom style library is to provide the 
`stylelib_url` parameter when calling `use` or `temp`, e.g.
```python
import mpls
mpls.use(context='a4', style='thesis', stylelib_url='http://some.other.repository.com/stylelib/{type}_{name}.json')
```

If you want to switch the style library for a longer session, it is more convenient to change the default `stylelib_url` in your
`mpls` configuration, i.e.
```python
import mpls
...
# switch to another remote stylelib temporarily
mpls.configure(stylelib_url='http://some.other.repository.com/stylelib/{type}_{name}.json')

# or switch to a local stylelib
mpls.configure(stylelib_url='~/stylelib/{type}/{name}.json')
```
It is important to specify the two placeholders `{type}` and `{name}` in the url, because internally `mpls` will 
substitute these placeholders with the parameters provided in the frontend methods. For example, the call
```python
mpls.use(context='a4')
```
boils down to
```python
mpls.get(name='a4', type='context')
```
which calls `stylelib_url.format(name=name, type=type)` (i.e. _str_.[format(*args, **kwargs)][4]) to replace the placeholders in the `stylelib_url`.

### Make your changes permanent
To make your changes permanent, just provide the `save=True` parameter when switching the `stylelib_url` in the
configuration or call `configure` later, i.e.
```
# save changes immediately
mpls.configure(stylelib_url='~/path/to/stylelib/{type}_{name}.json', save=True)
# or later
mpls.configure(stylelib_url='~/path/to/stylelib/{type}_{name}.json')
...
mpls.configure(save=True)
```
This will save your changes to the `mpls` configuration file and which is loaded every time `mpls` is initialized.

[1]: http://seaborn.pydata.org
[2]: http://matplotlib.org
[3]: http://matplotlib.org/users/customizing.html
[4]: https://docs.python.org/3.7/library/stdtypes.html?highlight=str.format#str.format

