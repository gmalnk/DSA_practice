from merge_sort import merge_sort_fun
def find_three_sums_brute_force(my_array,target):
    returning_set = set()
    for i in range(len(my_array)):
        for j in range(i+1, len(my_array)):
            for k in range(j+1, len(my_array)):
                if(my_array[i]+my_array[j]+my_array[k] == target):
                    returning_set.add((my_array[i], my_array[j], my_array[k]))
    return returning_set

def find_three_sums_On_2(my_array, target):
    sorted_array = merge_sort_fun(my_array)
    returning_set = set()
    for i in range(len(sorted_array)):
        lo = i+1
        hi = len(sorted_array)-1
        for j in range(i+1,len(sorted_array)):
            if (lo == hi):
                break
            RHS = target-sorted_array[i]
            if (sorted_array[lo]+sorted_array[hi] == RHS):
                returning_set.add((sorted_array[i],sorted_array[lo],sorted_array[hi]))
                lo += 1
            elif(sorted_array[lo]+sorted_array[hi] > RHS):
                hi -= 1
            else:
                lo += 1
    return returning_set
            
                
            
                 
# print(find_three_sums_brute_force([1,-1,2,-2,0,0,1,2,2],0))
ans = find_three_sums_On_2([-1,0,1,2,-1,-4],0)

print(ans)
# print(merge_sort_fun([1,-1,2,-2,0,0,1,2,2]))