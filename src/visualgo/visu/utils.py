import logging


def always_try(f):
    def decorated(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except Exception as ignored:
            logging.error("An error occurred:", exc_info=True)
    return decorated
