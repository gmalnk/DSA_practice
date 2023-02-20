
def Pascal_Triangle(a):
    array =[1,1]
    print([1])
    print([1,1])
    for i in range(2,a):
        array_to_print = [1]
        for i in range(len(array)-1):
            array_to_print.append(array[i]+array[i+1])
        array_to_print.append(1)
        array = array_to_print
        print(array_to_print)
            
        
Pascal_Triangle(20)