import sys
import random
import timeit

my_list = [23,45,100,45,90]
MAX_INT = sys.maxsize
print(my_list)
def find_min(my_list):
    min_index = -1
    min_val = MAX_INT
    for(i,v) in enumerate(my_list):
        if v < min_val:
            min_index = i
            min_val = v
    return min_index


#in the worst case it will go down the whole list, so for a list of n elements
# it is 0(n)
#  we will create a 100 random lists and find the minimum in each of them, averaging
#the time required

total_elapsed = 0
for i in range(100):
    my_list = list(range(10000))
    #put the elements of the list in random order
    random.shuffle(my_list)
    start = timeit.default_timer()
    min_index = find_min(my_list)
    end = timeit.default_timer()
    total_elapsed += end - start

print(total_elapsed /100 , "seconds")
