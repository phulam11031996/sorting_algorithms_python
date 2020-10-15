# This function is selection sort algorithms.
# Time complexity: O(n*n)
# Space complexity: O(1)
# When we use selection sort:
#   + small arrays where run time will be negligible no matter what algorithm is used.
#   + when array is kind of sorted.
#   + better to used than bubble sort when the cost of swapping elements are not expensive.
def selection_sort(arr):

    for i in range(0, len(arr)):
        k = i   # default smallest value is at the beginning of the array
        for j in range(i,len(arr)):
            if arr[k] >= arr[j]:
                k = j   # keeping track of index contains the smallest number

        arr[i], arr[k] = arr[k], arr[i] # swap the value
    return arr

my_array = [1,2,6,8,3,7,9]

print(selection_sort(my_array))