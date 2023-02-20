def find_reverse_pairs(my_array):
    counter = 0
    for i in range(0,len(my_array)):
        for j in range(i,len(my_array)):
            if(my_array[i]> 2*my_array[j]):
                counter += 1
    return counter

print(find_reverse_pairs([4,7,1,3,13,0]))
    