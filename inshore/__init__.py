# set the github repository variables
REPO_URL = "https://github.com/scruffy-t/inshore/"
BASE_URL = "https://raw.githubusercontent.com/scruffy-t/inshore/master/"
DATA_URL = BASE_URL + "{type}/{category}/{name}.json"


from .get import get
from .deploy import deploy

__all__ = [
    "get",
    "deploy"
]

__version__ = "0.1.0a1"
