def get_frequency_dict(my_array):
    returning_dict = {}
    for i in range(len(my_array)):
        returning_dict[my_array[i]] = []
    for i in range(len(my_array)):
        returning_dict[my_array[i]].append(i)
        
    return returning_dict
def find_two_sum(my_array, target):
    frequency_dict = get_frequency_dict(my_array)
    for i in range(len(my_array)):
        diff = target - my_array[i]
        if diff*2 == target and diff in frequency_dict.keys() and len(frequency_dict[diff])>1:
            return [frequency_dict[diff][0],frequency_dict[diff][1]]
        elif(diff in frequency_dict.keys() and len(frequency_dict[diff])!=0):
            return[i,frequency_dict[diff][0]]
    return []
            
            
            
print(find_two_sum([1,2,4,3,4,5],8))