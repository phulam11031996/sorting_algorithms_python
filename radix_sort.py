# This function is radix sort algorithms.
# Time complexity: In general, time compexity is all the same for radix sort
#                   Time complexity: O(n*k) k is the length of the largest number. However,
#                                   some camp believe k become logn. For more information see wiki.
#                   Space complexity: O(n*k) The amount of memory consumed by the algorithm increases 
#                                   relative to both the size of the input array and the length of the longest integer.
# When we use selection sort:
#   + Sort a list of any sort of binary data, including numeric, text, or image data in binary format.
#   + Sort a list of integers, and you don't know the value of the largest element in the list.
#        + If you do know the largest element in the list, see countingSort!

from random import randint
import math

def create_rand_int(size=10, max=100):
    '''
    DO: Create random numbers in an array
    PARA: size - how many numbers in the array, max - what is the range of the numbers
    RETURN: an array
    '''
    return [randint(0,max) for i in range(size)]

def getMaxDigits(arr):
    maxDigit = 0
    for i in arr:
        maxDigit = max(maxDigit, len(str(i)))
    return maxDigit

def getDigitFrom(num, i):
    return math.floor(abs(num) / pow(10, i)) % 10

def radix_sort(arr):
    '''
    DO: Use radix sort algorithms to sort an non-negative integer
    PARA: arr - an array
    RETURN: an array
    '''
    if not isinstance(arr, list):   # check if the para is an array
        return None

    for i in range(getMaxDigits(arr)):  # the length of maximun num in the array
        buckets = [[] for i in range(10)]   # reset the buckets
        for num in arr:     # putting the number in its bucket
            digit = getDigitFrom(num, i)
            buckets[digit].append(num)

    return_arr = []
    for i in buckets:   # faternning the array
        return_arr.extend(i)

    return return_arr



arr = create_rand_int()
print('Unsorted array: {}'.format(arr))
print('Sorted array  : {}'.format(radix_sort(arr)))