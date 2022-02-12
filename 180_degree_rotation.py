matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
lenMatrix=len(matrix)
for i in range(lenMatrix-1,-1,-1):
    for j in range(lenMatrix-1,-1,-1):
        print(matrix[i][j])