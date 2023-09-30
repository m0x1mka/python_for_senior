import functools


class MaxRetriesException(Exception):
    pass


def retry(times):
    def call_times(func):
        @functools.wraps(func)
        def decorate(*args, **kwargs):
            for _ in range(times):
                try:
                    ans = func(*args, **kwargs)
                except:
                    pass
                else:
                    return ans
            else:
                raise MaxRetriesException

        return decorate

    return call_times
