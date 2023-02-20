
def find_routs(i,j):
    
    if i ==1 or j == 1 :
        return 1
    if i<1 or j<1:
        return 0
    return find_routs(i-1,j)+find_routs(i,j-1)

print(find_routs(2,100))