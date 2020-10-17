# This function is quick sort algorithms.
# Time complexity: Best case - O(nlogn)
#                   Worst case - O(n*n)
# Space complexity: O(n)
# When we use selection sort:
#   + Study shown quick sort are faster than merge sort when we randomly chose a pivot.
#   + When we know some constraints about dataset and we can make some modifications to pick the best pivot.

from random import randint

def create_random_array(size=10, max=50):   # size is how many number in the array. max is the maximun range of the array
    '''
    DO: Return random unsorted array.
    PARA: size - the size of the array, max - the maximum range of the array
    OUT: An array of random integer
    '''
    return [randint(0,max) for i in range(size)]

def quick_sort(arr):
    '''
    DO: Use quick sort algrothims to sort the array
    PARA: arr - an array of integer
    OUT: An array of sorted integer
    '''
    if len(arr) <= 1:   # This is the base case.
        return arr

    pivot = arr.pop(0)  # We chose the fit element in the array as the pivot.
    left = [arr[i] for i in range(len(arr)) if arr[i]<pivot]    # Putting all smaller numbers to the left.
    right = [arr[i] for i in range(len(arr)) if arr[i]>=pivot]  # Putting all larger numbers to the right.

    return quick_sort(left) + [pivot] + quick_sort(right)   # Recursively caling the function.

arr = create_random_array() # Create random integer
print('Unsorted array: {}'.format(arr))
print('Sorted array:   {}'.format(quick_sort(arr)))



    

