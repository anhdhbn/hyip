from .base import Driver, handle_exceptions


class Wrapper:
    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, item):
        prop = getattr(self.obj, item)
        if callable(prop):
            def unraisable(*args, **kwargs):
                try:
                    return prop(*args, **kwargs)
                except Exception as e:
                    self.obj.quit()
                    raise(e)

            return unraisable

        return prop