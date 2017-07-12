from .config import REPO_URL


class MPLSError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)
        self.message = message


class MPLSDecodeError(MPLSError):

    MESSAGE = """
    {type} file at {data_url} is not valid:
      {err_msg}
    Please report this at {repo_url}.
    """

    def __init__(self, type, data_url, err_msg, repo_url=REPO_URL):
        message = self.MESSAGE.format(type=type, data_url=data_url, err_msg=err_msg, repo_url=repo_url)
        MPLSError.__init__(self, message)


class MPLSNotFoundError(MPLSError):

    MESSAGE = """
    could not find {type} file at {data_url}:
      {err_msg}
    Please browse {repo_url} for available {type} files.
    """

    def __init__(self, type, data_url, err_msg, repo_url=REPO_URL):
        message = self.MESSAGE.format(type=type, data_url=data_url, err_msg=err_msg, repo_url=repo_url)
        MPLSError.__init__(self, message)
