#https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/?envType=daily-question&envId=2025-08-20
def countSquares(matrix):
    if (len(matrix) == 0):
        return 0
    #print(len(matrix))
    #print(len(matrix[0]))

    #grab max size

    max_size = max(len(matrix),len(matrix[0]))
    
    #run conv on all 1's until max size is the size of the square
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


mat = [[0,1],[1,1],[0,1]]
print(countSquares(mat))