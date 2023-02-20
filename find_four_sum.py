def find_four_sum(my_array, target):
    returning_set = set()
    for i in range(len(my_array)):
        sum=0
        for j in range(i+1,len(my_array)):
            for k in range(j+1,len(my_array)):
                for l in range(k+1,len(my_array)):
                    sum = my_array[i]+my_array[j]+my_array[k]+my_array[l]
                    if(sum == target):
                        returning_set.add((my_array[i],my_array[j],my_array[k],my_array[l]))
    return returning_set

print(find_four_sum([1,0,-1,0,-2,2],0))