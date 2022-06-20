#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        ans = fct(*args)
    except Exception as error:
        sys.stderr.write("Exception: {}\n".format(error))
        ans = None

    return (ans)
