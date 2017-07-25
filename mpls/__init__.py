from .version import __version__
from .cache import clear_cache
from .config import configure
from .mpls import get, use, temp

__all__ = [
    "clear_cache",
    "configure",
    "get",
    "use",
    "temp"
]
