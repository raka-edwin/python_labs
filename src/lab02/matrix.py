def transpose(mat):
    if len(mat)==0:
        return []
    else:
        m=len(mat)
        n=len(mat[0])
        mat2=[[0 for i in range(m)]for i in range(n)]
        for x in range(0,m):
            for y in range(0,n):
                mat2[y][x]=mat[x][y]
        return mat2

def row_sums(mat):
    m=len(mat)
    matrix_row_sum=[[]for i in range(m)]
    for i in range(0,m):
        matrix_row_sum[i].append(sum(mat[i]))
    return matrix_row_sum

matrix1=[[[1,2,3]],[[1],[2],[3]],[[1,2],[3,4]],[],[[1,2],[3]]]
matrix2=[[[1,2,3],[4,5,6]],[[-1,1],[10,-10]],[[0,0],[0,0]],[[1,2],[3]]]

lencheck1=[[]for i in range(len(matrix1))]
for x in range(0,len(matrix1)):
    for y in range(0,len(matrix1[x])):
        lencheck1[x].append(len(matrix1[x][y]))

lencheck2=[[]for i in range(len(matrix2))]
for x in range(0,len(matrix2)):
    for y in range(0,len(matrix2[x])):
        lencheck2[x].append(len(matrix2[x][y]))

print("transpose")
for x in range(0,len(lencheck1)):
    if len(set(lencheck1[x]))<=1:
        print(matrix1[x]," → ",transpose(matrix1[x]))
    else:
        print(matrix1[x]," → ",ValueError)
print(" ")
print("row_sums")
for x in range(0,len(lencheck2)):
    if len(set(lencheck2[x]))<=1:
        print(matrix2[x]," → ",row_sums(matrix2[x]))
    else:
        print(matrix2[x]," → ",ValueError)
print(" ")
print("col_sums")
for x in range(0,len(lencheck2)):
    if len(set(lencheck2[x]))<=1:
        print(matrix2[x]," → ",row_sums(transpose(matrix2[x])))
    else:
        print(matrix2[x]," → ",ValueError)
#запуск      py .\src\lab02\matrix.py