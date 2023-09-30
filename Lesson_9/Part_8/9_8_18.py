import functools


def make_html(tag):
    def add_tag(func):
        @functools.wraps(func)
        def decorate(*args, **kwargs):
            ans = func(*args, **kwargs)
            return f"<{tag}>" + ans + f"</{tag}>"
        return decorate
    return add_tag




