import pstats, cProfile, io

def profile(fnc):
    """
    An implementation of a function decorator that wraps a function in
    a code that profiles it.
    """
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()

        # wrapped function starts
        retval = fnc(*args, **kwargs) #fnc is whatever function has the @profile tag
        # wrapped function ends

        pr.disable()
        s = io.StringIO()
        sortby = pstats.SortKey.CALLS
        ps = pstats.Stats(pr, stream=s).strip_dirs().sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner

#profile function is called first, passing in heavy_function as its parameter
@profile
def heavy_function():
    for x in range(0,1000):
        for y in range(0,100):
            for z in range(0,100):
                z += x + y

#profile function is called first, passing in heavy_function_2 as its parameter
@profile
def heavy_function_2():
    for a in range(0,1000):
        for b in range(0,100):
            for c in range(0,100):
                c += a * b

def main():
    heavy_function() #when heavy_function is executed it's first wrapped in the profile function, then executed
    pass

if __name__ == '__main__':
    main()



