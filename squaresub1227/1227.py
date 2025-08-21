#https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/?envType=daily-question&envId=2025-08-20
'''
def countSquares(matrix):
    if (len(matrix) == 0):
        return 0
    max_size = max(len(matrix),len(matrix[0]))
    
    conv = 1
    sub_arrays = []
    while conv <= max_size:
        #extract square
        for i in range(len(matrix)- conv + 1):
            for j in range(len(matrix[i]) - conv + 1):
                sub = [row[j:j+conv] for row in matrix[i:i+conv]]
                sub_arrays.append(sub)
        conv += 1
    print(sub_arrays)
    count = 0
    for sub in sub_arrays:
        all_ones = True
        for i in sub:
            for j in i:
                if j == 0:
                    all_ones = False
                    break
        if all_ones == True:
            count += 1
    return count

mat = [[0,1],[1,1],[0,1]]

print(countSquares(mat))#https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/?envType=daily-question&envId=2025-08-20


'''
def countSquares(matrix):
    if (len(matrix) == 0):
        return 0
    max_size = min(len(matrix),len(matrix[0]))
    
    conv = 1
    sub_arrays = []
    while conv <= max_size:
        for i in range(len(matrix)- conv + 1):
            for j in range(len(matrix[i]) - conv + 1):
                if matrix[i][j] == 1:
                    sub = [row[j:j+conv] for row in matrix[i:i+conv]]
                    sub_arrays.append(sub)
        conv += 1
    #print(sub_arrays)
    count = 0
    for sub in sub_arrays:
        all_ones = True
        for i in sub:
            for j in i:
                if j == 0:
                    all_ones = False
                    break
        if all_ones == True:
            count += 1
    return count

mat =[[1,0,1],[1,1,0],[1,1,0]]
print(countSquares(mat))