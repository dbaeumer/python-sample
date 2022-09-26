# ImpSort objects are used to perform sorting operations
# TimeOutException can be used to detect timeouts
from ImpSort import (ImpSort, TimeOutException)

# The default algorithm is 'rand_swap'
# You can alternatively set it as 'bogo' or 'recompile'
# You can also provide a random to use (such as a random.SystemRandom instance)
sorter = ImpSort()

unsorted_list = [24, 106, 2, 42]  # This is a sample unsorted list

# To simply sort the list:
sorter.sort(unsorted_list)

# To get metadata about the most recent run, use the meta attribute:
print(sorter.meta)

# To get each iteration as the sort progresses, use the sort_generator method to get an iterable
for u in sorter.sort_generator(unsorted_list):
    print(u)

# To set a timeout, use the timeout argument:
try:
    # This will time out if it hasn't returned in 10 seconds
    sorter.sort(unsorted_list, timeout=10)
except TimeOutException as e:
    # You can catch a TimeOutException
    print(e)  # The exception includes some statistics about the failed run