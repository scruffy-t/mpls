import json
import urllib
from urllib.request import urlopen

from . import REPO_URL, BASE_URL, DATA_URL


def __get(name, category, type, **kwargs):
    """

    Notes
    -----

    A list of scientific journal name abbreviations can be found here:
        https://images.webofknowledge.com/images/help/WOS/A_abrvjt.html
    """
    data_url = kwargs.get('data_url', DATA_URL).format(type=type, category=category, name=name)
    repo_url = kwargs.get('repo_url', REPO_URL)

    json_msg = """
    {type} file at {url} is not valid:
      {err_msg}
    Please report this at {repo_url}.
    """

    url_msg = """
    could not read {type} file at {url}:
      {err_msg}
    Please browse {repo_url} for available {type} files.
    """

    try:
        with urlopen(data_url) as url:
            # get file content from specified url
            content = url.read().decode()
            try:
                # convert file content to python dict
                context = json.loads(content)
            except json.JSONDecodeError as e:
                raise IOError(json_msg.format(url=data_url, err_msg=e.msg, repo_url=repo_url))
        return context
    except urllib.error.HTTPError as e:
        raise IOError(url_msg.format(url=data_url, err_msg=e.msg, repo_url=repo_url))


def get(name, category='paper', type=('context', 'style', 'palette')):
    """
    """
    if isinstance(type, tuple) or isinstance(type, list):
        return {t: __get(name, category, t) for t in type}
    elif isinstance(type, str) and type in ('context', 'style'):
        return __get(name, category, type)
    raise ValueError('the type argument must either be a tuple/list or a str')
