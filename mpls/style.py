


class StyleComponent(object):

    def __init__(self, params):
        self._p = params

    def __getitem__(self, key):
        return self._p[key]

    def edit(**kwargs):
        for key, value in kwargs.items():
            getattr(self, key)(value)

    @classmethod
    def validate(cls, params):
        pass


class Context(StyleComponent):

    def __init__(self, params):
        StyleComponent.__init__(self, params)

    def scale(self, factor):
        pass

    def flip(self, flip):
        pass


class Style(StyleComponent):

    def __init__(self, params):
        StyleComponent.__init__(self, params)


class Palette(StyleComponent):

    def __init__(self, params):
        StyleComponent.__init__(self, params)

    def desaturate(self, factor):
        pass

    def revert(self, revert):
        pass
