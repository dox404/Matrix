matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
lenMatrix=len(matrix)
# for i in range(3,0,-1):
# list=[1,2,3]
for j in range(lenMatrix):
    for i in range(lenMatrix-1,-1,-1):
    
     print(matrix[i][j])