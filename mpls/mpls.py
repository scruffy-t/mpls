"""
"""
from urllib.request import urlopen, URLError, HTTPError

from .utils import remove_comments
from .cache import CACHE
from .config import CONFIG, MPLS_STYPES

import json
import matplotlib as mpl
import matplotlib.style
import logging

logger = logging.getLogger(__name__)


def __get(name, stype, **kwargs):
    """

    Parameters
    ----------
    name: str

    stype: str

    kwargs:
    - style_url: str

    - stylelib_url: str

    - stylelib_format: str

    - ignore_cache: bool

    Raises
    ------
    IOError:
    HTTPError:
    URLError:
    JSONDecodeError:
    """
    folder    = kwargs.get('stylelib_url', CONFIG['stylelib_url'])
    file_path = kwargs.get('stylelib_format', CONFIG['stylelib_format'])
    style_url = kwargs.get('style_url', folder+file_path).format(stype=stype, name=name)

    if not kwargs.get('ignore_cache', False) and CACHE.is_cached(stype, name):
        logger.debug('loading {} file from cache'.format(stype))
        with open(CACHE.file_path(stype=stype, name=name), 'r') as f:
            content = remove_comments(f.read())
    else:
        try:
            logger.debug('trying to urlopen file: {}'.format(style_url))
            with urlopen(style_url) as f:
                # get file content from specified url
                content = remove_comments(f.read().decode())
            logger.debug('loaded raw {} file from URL'.format(stype))
            CACHE.add(stype, name, content)
        except ValueError as e:  # style_url is not a valid url
            logger.debug('urlopen failed: {}'.format(str(e)))
            logger.debug('trying to (regular) open file')
            try:
                with open(style_url) as f:
                    # get file content from file path instead
                    content = remove_comments(f.read())
                logger.debug('loaded file from local disk'.format(stype))
            except IOError:
                raise
        except HTTPError as e:
            raise
        except URLError as e:
            logger.debug('urlopen failed: {}'.format(str(e)))
            raise

    try:
        logger.debug('converting file content to Python dict')
        # convert file content to python dict
        return json.loads(content)
    except json.JSONDecodeError as e:
        logger.debug('json.loads failed: {}'.format(str(e)))
        raise


def get(name, stype, **kwargs):
    """Returns the rcParams specified in the style file given by `name` and `stype`.

    Parameters
    ----------
    name: str
        The name of the style.
    stype: str
        Any of ('context', 'style', 'palette').
    kwargs:
    - stylelib_url: str
        Overwrite the value in the local config with the specified url.
    - ignore_cache: bool
        Ignore files in the cache and force loading from the stylelib.

    Raises
    ------
    ValueError:
        If `stype` is not any of ('context', 'style', 'palette')

    Returns
    -------
    rcParams: dict
        The parameter dict of the file.
    """
    stype = str(stype)

    params = {}
    if stype in MPLS_STYPES:
        params.update(__get(name, stype, **kwargs))
    else:
        raise ValueError('unexpected stype: {}! Must be any of {!r}'.format(stype, MPLS_STYPES))

    # color palette hack
    if params.get('axes.prop_cycle'):
        params['axes.prop_cycle'] = mpl.rcsetup.cycler('color', params['axes.prop_cycle'])

    return params


def collect(context=None, style=None, palette=None, **kwargs):
    """Returns the merged rcParams dict of the specified context, style, and palette.

    Parameters
    ----------
    context: str

    style: str

    palette: str

    kwargs:
    -

    Returns
    -------
    rcParams: dict
        The merged parameter dicts of the specified context, style, and palette.

    Notes
    -----
    The rcParams dicts are loaded and updated in the order: context, style, palette. That means if
    a context parameter is also defined in the style or palette dict, it will be overwritten. There
    is currently no checking being done to avoid this.
    """
    params = {}
    if context:
        params.update(get(context, 'context', **kwargs))
    if style:
        params.update(get(style, 'style', **kwargs))
    if palette:
        params.update(get(palette, 'palette', **kwargs))
    return params


def use(*args, context=None, style=None, palette=None, **kwargs):
    """

    Parameters
    ----------
    args:

    context: str or None

    style: str or None

    palette: str or None

    kwargs:
    - reset

    Raises
    ------
    ValueError:

    """
    if kwargs.get('reset', False):
        styles = ['default', ]
    else:
        styles = []

    styles.extend(list(args))
    styles.append(collect(context=context, style=style, palette=palette, **kwargs))
    # apply mpls styles
    return mpl.style.use(styles)


def temp(*args, context=None, style=None, palette=None, **kwargs):
    """

    Parameters
    ----------
    args:

    context: str or None

    style: str or None

    palette: str or None

    kwargs:
    - reset

    Raises
    ------
    ValueError:

    """
    # apply specified matplotlib styles and reset if specified
    styles = list(args)
    styles.append(collect(context=context, style=style, palette=palette, **kwargs))
    return mpl.style.context(styles, after_reset=kwargs.get('reset', False))
