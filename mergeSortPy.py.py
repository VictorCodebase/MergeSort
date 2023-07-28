
#python


sample_data = [9,3,2,5,7,11,4,6];

def merge_sort(arr):
    if len(arr) > 1:

        left_arr = arr[:len(arr)//2]#first sub array from begining of original array to mid
        right_arr = arr[len(arr)//2:]#first sub array from begining of original array to mid

        #! RECURSION
        merge_sort(left_arr)
        merge_sort(right_arr)

        #! MERGE
        #? Here we compare the left most element of both left and right arrs
        i = 0 # keep track of left index
        j = 0 # keep track of right index
        k = 0 # merged array index

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
print(sample_data)
merge_sort(sample_data)
print(sample_data)