import json
import urllib
import re
import matplotlib as mpl
import matplotlib.pyplot as plt
from os.path import join as pjoin
from urllib.request import urlopen, HTTPError

from .utils import remove_comments
from .config import REPO_URL, DATA_URL, MPLS_TYPES
from .exceptions import MPLSNotFoundError, MPLSDecodeError


def __get(name, category, type, **kwargs):
    """
    """
    data_url = kwargs.get('data_url', DATA_URL).format(type=type, category=category, name=name)
    repo_url = kwargs.get('repo_url', REPO_URL)

    try:
        f = urlopen(data_url)
        # get file content from specified url
        content = remove_comments(f.read().decode())
    except HTTPError as e:
        raise MPLSNotFoundError(
            type=type,
            data_url=data_url,
            err_msg=e.msg,
            repo_url=repo_url
        )
    except ValueError:
        try:
            f = open(data_url)
            # get file content from specified path
            content = remove_comments(f.read())
        except OSError:
            raise MPLSNotFoundError(
                type=type,
                data_url=data_url,
                err_msg='Given data_url is not valid!',
                repo_url=repo_url
            )
    try:
        # convert file content to python dict
        context = json.loads(content)
    except json.JSONDecodeError as e:
        raise MPLSDecodeError(type=type, data_url=data_url, err_msg=e.msg, repo_url=repo_url)

    f.close()
    return context


def get(name, category='', type=None, **kwargs):
    """

    Parameters
    ----------
    name: str

    category: str

    type: tuple-of-str, str, None (default)

    Raises
    ------
    ValueError:

    MPLSNotFoundError:
    """
    rcparams = {}
    if isinstance(type, (tuple, list)):
        for t in type:
            rcparams.update(__get(name, category, t, **kwargs))
    elif isinstance(type, str):
        if type in MPLS_TYPES:
            rcparams.update(__get(name, category, type, **kwargs))
        else:
            raise ValueError('Unexpected type "{}"! Must be any of {:!r}'.format(MPLS_TYPES))
    elif type is None:
        for t in MPLS_TYPES:
            try:
                rcparams.update(__get(name, category, t, **kwargs))
            except MPLSNotFoundError:
                continue
    else:
        raise ValueError('The type argument must either be a tuple/list, str, or None')

    if len(rcparams) == 0:
        raise MPLSNotFoundError()

    # color palette hack
    if rcparams.get('axes.prop_cycle'):
        rcparams['axes.prop_cycle'] = mpl.rcsetup.cycler('color', rcparams['axes.prop_cycle'])

    return rcparams


def use(name, category='', type=None, **kwargs):
    """
    """
    return plt.style.use(get(name, category, type, **kwargs))


def context(name, category='', type=None, **kwargs):
    """
    """
    return plt.style.context(get(name, category, type, **kwargs))
