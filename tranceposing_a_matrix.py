matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]]

matrix_length=len(matrix)
    

for i in range(matrix_length):
    for j in range(matrix_length):
        # print(i,j)
        # print(matrix[i][j])
        
        print(matrix[j][i])
        print('\t')
    print('\t')
    # print(i)
