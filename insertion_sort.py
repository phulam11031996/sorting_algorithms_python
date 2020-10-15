# This function is insertion sort algorithms.
# Time complexity: O(n*n)
# Space complexity: O(1)
# When we use selection sort:
#   + used when there is ONLY one unsorted element. O(n)
#   + used when date is live and constantly push. O(n)
#   + used when array is kind of sorted
#   + used when small arrays where run time will be negligible no matter what algorithm we choose
def insertion_sort(arr):
    
    for i in range(1,len(arr)):
        current_ele = arr[i]    # keeping track of the current element

        j = i - 1   # creating the range for the innner loop
        while(current_ele < arr[j] and j >= 0):
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = current_ele    # refill the missing spot with the current element

    return arr

my_array = [1,2,6,3,7,9,4,3]

print(insertion_sort(my_array))