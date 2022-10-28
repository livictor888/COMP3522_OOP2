import pstats, cProfile, io
from pstats import SortKey

def heavy_function():
    for x in range(0,1000):
        for y in range(0,100):
            for z in range(0,100):
                z += x + y

def heavy_function_2():
    for a in range(0,1000):
        for b in range(0,100):
            for c in range(0,100):
                c += a * b

def main():
    pr = cProfile.Profile()
    pr.enable()

    # … code to be profiled comes here …
    heavy_function()
    # … end code to be profiled …

    pr.disable()
    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).strip_dirs().sort_stats(sortby)
    ps.print_stats()  # print to the StringIO output stream ‘s’.
    print(s.getvalue())  # print the output stream ‘s’

if __name__ == '__main__':
    main()



