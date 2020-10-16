from random import randint

def create_random(size=10, max=99):
    '''
    DO: Return a ramdom array of numbers
    PARA: size - an int, max - an int
    OUT: A list of random numbers
    '''
    return [randint(0, max) for i in range(size)] # creating a list of ramdom numbers

# this function merges 2 sorted array.
def merge(left_arr, right_arr):
    '''
    DO: Merging 2 sorted arrays together
    PARA: left_arr - a sorted array, left_arr - a sorted array
    OUT: A new sorted array
    '''
    merged_arr = [] # result array

    left_idx = 0
    right_idx = 0
    while(left_idx < len(left_arr) and right_idx < len(right_arr)):
        if left_arr[left_idx] < right_arr[right_idx]:   # use left_idx and right_idx to and compare
            merged_arr.append(left_arr[left_idx])       #       to add to the end of the array
            left_idx += 1
        else:
            merged_arr.append(right_arr[right_idx])
            right_idx += 1

    merged_arr.extend(right_arr[right_idx:])    # adding the rest of element in the arrays
    merged_arr.extend(left_arr[left_idx:])      #   to the resulted array

    return merged_arr

def merge_sort(a):
    '''
    DO: Merge sorts an array
    PARAS: a - unsorted/sorted array
    OUT: a sorted array
    '''
    if len(a) == 1: return a    # Base case

    left, right = merge_sort(a[:len(a)//2]), merge_sort(a[len(a)//2:])  # recursive

    return merge(left, right)

my_arr = create_random()
print(my_arr)
print(merge_sort(my_arr))