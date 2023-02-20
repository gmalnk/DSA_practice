
def Matrix_Filder(aij):
    column_indexes = []
    row_indexes = []
    for i in range(len(aij)):
        result = 1
        for j in range(len(aij[0])):
            result *= aij[i][j]
        if result == 0:
            row_indexes.append(i)
    for i in range(len(aij[0])):
        result = 1
        for j in range(len(aij)):
            result *= aij[j][i]
        if result == 0:
            column_indexes.append(i)  
    print(row_indexes)
    print(column_indexes) 
    
    for i in range(len(aij[0])):
        for j in range(len(aij)):
            if(i in column_indexes or j in row_indexes):
                aij[j][i] = 0
    print(aij)

matrix = [[1,2,3],[0,5,6],[34,54,0],[4324,534,532]]
Matrix_Filder(matrix)   
       
        