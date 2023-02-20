import math
def search_array(arr,element):
    length = len(arr[0])
    start = 0
    end = len(arr)
    mid = math.floor((start+end)/2)
    while (True):
        if(element == arr[mid][length-1]):
            return mid
        if (element == arr[mid][0]):
            return mid
        if (element < arr[mid][length-1] and element > arr[mid][0]):
            return mid
        else:
            if(start == mid or mid == end):
                return -1
            if not element < arr[mid][length-1]:
                start = mid
            else:
                end = mid
        mid = math.floor((start+end)/2)

def search_element(arr, element):
    length = len(arr)
    start = 0
    end = len(arr)
    mid = math.floor((start+end)/2)
    while (True):
        
        if (element == arr[mid]):
            return mid
        else:
            if(start == mid or mid == end):
                return -1
            if element > arr[mid]:
                start = mid
            else:
                end = mid
        mid = math.floor((start+end)/2)

array =[[1,3,5,7],
 [10,11,16,20],
 [23,30,34,60]]
element = 7

i = search_array(array, element)
j = search_element(array[i], element)
print(i,j)