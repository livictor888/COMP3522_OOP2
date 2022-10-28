import cProfile
import re
import pstats

from pstats import SortKey

cProfile.run('re.compile("foo|bar")', 'restats')

p = pstats.Stats('restats')
p.print_stats()
# p.strip_dirs().sort_stats('ncalls').print_stats() #sorts ncalls in decending order
p.strip_dirs().sort_stats(SortKey.STDNAME).print_stats() #sorts by standard name