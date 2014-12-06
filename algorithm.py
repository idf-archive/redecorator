__author__ = 'Danyang'
def memoize(f):
    """
    the function must not modify or rely on external state 
    the function should be stateless. 
    usage: @memoize(function) as function annotation

    :param f: the function, whose result you would like to cached based on input arguments
    """
    cache = {}
    def ret(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return ret