import math
def merger_function(array1,array2):
    returning_array = []
    for i in range(len(array2)+len(array1)):
        if (len(array1)==0):
            returning_array+=array2
            break
        if (len(array2)==0):
            returning_array+=array1
            break
        if (array1[0]>array2[0]):
            min = array2[0]
            array2 = array2[1:]
        else:
            min = array1[0]
            array1 = array1[1:]
        returning_array.append(min)
    return returning_array
    
    
def breaker_function(my_array):
    length = len(my_array)
    if (length > 1):
        return(merger_function(breaker_function(my_array[:math.floor(length/2)]),breaker_function(my_array[math.floor(length/2):])))
    else:
        return my_array
    
def merge_sort(my_array):
    return(breaker_function(my_array))
    

print(merge_sort([4,8,9,6,5,2,3,1,7,10]))