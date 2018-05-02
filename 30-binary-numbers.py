#!/bin/python3

def decToBin(n):
    if n==0: return ''
    else:
        return decToBin(n/2) + str(n%2)

import sys
n = int(input().strip())
mystr = "{0:b}".format(n)
my_max_1s = 0
my_running_1s = 0
for mychar in mystr:
    if int(mychar) == 0:
        #print('-')
        my_running_1s = 0
        continue
    else:
       my_running_1s += 1
       if ( my_running_1s > my_max_1s ):
           my_max_1s = my_running_1s
    #print(mychar, my_running_1s, my_max_1s)
print(my_max_1s)
