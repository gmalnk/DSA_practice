import math
def merger_function(array1, array2):
    print(array1,array2)
    days = {}
    returning_array = []
    for i in range(len(array1)+len(array2)):
        if len(array1) ==0:
            returning_array += array2
            break
        if len(array2) == 0:
            returning_array += array1
            break
        if array1[0][1] == array2[0][1]:
            if (array1[0][2]>array2[0][2]):
                returning_array.append(array1[0])
                days[array1[0][1]] =0
                array1 = array1[1:]
            else:
                returning_array.append(array2[0])
                days[array2[0][1]] =0
                array2 = array2[1:]
        elif(array1[0][1] < array2[0][1]):
            if (array2[0][1] in days.keys() and array1[0][2] > array2[0][2]):
                returning_array.append(array1[0])
                days[array1[0][1]] =0
                array1 = array1[1:]
            else:
                returning_array.append(array2[0])
                days[array2[0][1]] =0
                array2 = array2[1:]
        elif (array2[0][1] < array1[0][1]):
            if (array1[0][1] in days.keys() and array2[0][2] > array1[0][2]):
                returning_array.append(array2[0])
                days[array2[0][1]] =0
                array2 = array2[1:]
            else:
                returning_array.append(array1[0])
                days[array1[0][1]] =0
                array1 = array1[1:]
    return returning_array
            
        

def divider_func(my_array):
    print(my_array)
    if len(my_array) > 1:
       return merger_function(divider_func(my_array[:math.floor(len(my_array)/2)]),divider_func(my_array[math.floor(len(my_array)/2):]))
    else:
        return my_array

def get_sorted_jobs(my_array):
     return divider_func(my_array)

def find_best_job_sequencing(my_array):
    sorted_array = get_sorted_jobs(my_array)

    print(sorted_array)
    my_total_profit = 0
    no_of_working_days = 0
    day = sorted_array[0][1]
    for i in range(0,sorted_array[0][1]):
        if day > 0:
            # print(day)
            if(day <= sorted_array[0][1]):
                # print("yes")
                no_of_working_days += 1
                my_total_profit += sorted_array[0][2]
                sorted_array = sorted_array[1:]
            day -=1
        elif day==0:
            break

            
    return [no_of_working_days, my_total_profit]
                
    
print(find_best_job_sequencing([[1,2,100],[20,4,19],[3,4,27],[4,1,25],[5,1,15]]))
        