
def Kadanes_Algorithm(arr):
    gmax = 0
    for i in range(len(arr)):
        lmax = arr[i]
        sum = arr[i]
        for j in range(i+1,len(arr)):
            sum = sum + arr[j]
            if sum > lmax :
                lmax = sum
        if lmax > gmax:
            gmax = lmax
    print(gmax)
Kadanes_Algorithm([34,-523,23,-345,2345,-32,5234,5,-32,-323,-45,2,345,234,5,234,5234,-5,-23,-45,-2,3,-45,-23,-45,-2,-34,-523,-7857,23,5,-235,23,-4,5])