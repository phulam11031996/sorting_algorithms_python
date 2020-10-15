# This function is a bubble sort.
# Time complexity: O(n*n)
# Space complexity: O(1)
# When we use bubble sort:
#   + small arrays where run time will be negligible no matter what algorithm is used.
#   + when array is kind of sorted.

def bubble_sort(arr):
    is_sorted = True  # this variable will be used to enter in while loop.

    while (is_sorted):
        is_sorted = False    # assume the array is sorted.

        for index in range(0,len(arr)-1):   
            if arr[index] > arr[index+1]:
                arr[index], arr[index+1] = arr[index+1], arr[index]
                is_sorted = True 
                
    return arr

my_array = [2,4,7,3,4,6,2,4]

print(bubble_sort(my_array))