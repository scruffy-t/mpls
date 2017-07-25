import os
import json
import sys
import logging

logger = logging.getLogger(__name__)

try:
    import seaborn
    HAS_SEABORN = True
    if 'seaborn' in sys.modules:
        SEABORN_LOADED = True
    else:
        SEABORN_LOADED = False
except ImportError:
    HAS_SEABORN = False
    SEABORN_LOADED = False

MPLS_TYPES = ('context', 'style', 'palette')

CONFIG_DIR = os.path.expanduser('~/.mpls')
CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.json')

CACHE_DIR = os.path.join(CONFIG_DIR, 'cache')

DEFAULT_CONFIG = {
    'stylelib_url': "https://raw.githubusercontent.com/scruffy-t/mpls/master/stylelib/{type}/{name}.json",
    'enable_cache': True,
    'enable_logging': True
}

try:
    CONFIG = json.load(open(CONFIG_FILE, 'r'))
    logger.debug('using custom config {}'.format(CONFIG_FILE))
except OSError:
    CONFIG = DEFAULT_CONFIG
    logger.debug('using default config')

if CONFIG['enable_logging']:
    logging.basicConfig(level=logging.DEBUG)


def configure(save=False, **kwargs):
    """

    Parameters
    ----------
    save: bool
        Save config to file after it was updated
    kwargs:

    """
    CONFIG.update(kwargs)
    if save:
        if not os.path.exists(CONFIG_DIR):
            os.mkdir(CONFIG_DIR)
        json.dump(CONFIG, open(CONFIG_FILE, 'w'))
        logger.debug('saved custom config to {}'.format(CONFIG_FILE))
