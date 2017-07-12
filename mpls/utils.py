import re
import os

from .config import DATA_BASE_URL


def remove_comments(text):
    """Remove C and Javascript style comments like // [...] and /* [...] */ from
    the given text.

    https://stackoverflow.com/questions/2319019/using-regex-to-remove-comments-from-source-files
    """
    pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
    # first group captures quoted strings (double or single)
    # second group captures comments (//single-line or /* multi-line */)
    regex = re.compile(pattern, re.MULTILINE|re.DOTALL)
    def _replacer(match):
        # if the 2nd group (capturing comments) is not None,
        # it means we have captured a non-quoted (real) comment string.
        if match.group(2) is not None:
            return "" # so we will return empty to remove the comment
        else: # otherwise, we will return the 1st group
            return match.group(1) # captured quoted-string
    return regex.sub(_replacer, text)


def all_styles(stylelib=DATA_BASE_URL):
    """
    """
    styles = []
    for category in os.scandir(stylelib):
        if category.is_dir():
            for name in os.scandir(os.path.join(stylelib, category.path)):
                if name.is_file() and name.path.endswith('.json'):
                    cat = os.path.basename(category.path)
                    style = os.path.basename(name.path).split('.')[0]
                    styles.append((cat, style))
    return set(styles)
