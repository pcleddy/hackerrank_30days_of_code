#!/bin/python3

import sys

my_debug = 0

def get_hourglasses(arr):
    max_hg = -999
    for row_index in range(1, len(arr) - 1):
        #print(row_index)
        #print (arr[row_index])
        for column_index in range(1, len(arr[row_index]) - 1):
            if my_debug: print(row_index, column_index)
            hourglass = [ \
              arr[row_index - 1][column_index - 1], \
              arr[row_index - 1][column_index], \
              arr[row_index - 1][column_index + 1], \
              arr[row_index][column_index], \
              arr[row_index + 1][column_index - 1], \
              arr[row_index + 1][column_index], \
              arr[row_index + 1][column_index + 1] \
            ]
            if my_debug: print(hourglass)
            hourglass_sum = sum(hourglass)
            if my_debug: print(hourglass_sum)
            if ( sum(hourglass) > max_hg ): max_hg = sum(hourglass)
    return max_hg

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

print(get_hourglasses(arr))
#print(arr)

