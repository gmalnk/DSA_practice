def find_three_sums_brute_force(my_array,target):
    returning_set = set()
    for i in range(len(my_array)):
        for j in range(i+1, len(my_array)):
            for k in range(j+1, len(my_array)):
                if(my_array[i]+my_array[j]+my_array[k] == target):
                    returning_set.add((my_array[i], my_array[j], my_array[k]))
    return returning_set
                
print(find_three_sums_brute_force([1,-1,2,-2,0,0,1,2,2],0))     