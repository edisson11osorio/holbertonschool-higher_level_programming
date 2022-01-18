def safe_function(fct, *args):
    from sys import stderr
    try:
        return fct(*args)
    except Exception as ex:
        print("Exception: {}".format(ex), file=stderr)
        return None
