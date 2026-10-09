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

def lencheck(mat):
    a=[[]for i in range(len(mat))]
    for x in range(0,len(mat)):
        for y in range(0,len(mat[x])):
            a[x].append(len(mat[x][y]))
    return a

matrix1=[[[1,2,3]],[[1],[2],[3]],[[1,2],[3,4]],[],[[1,2],[3]]]
matrix2=[[[1,2,3],[4,5,6]],[[-1,1],[10,-10]],[[0,0],[0,0]],[[1,2],[3]]]

print("transpose")
for x in range(0,len(lencheck(matrix1))):
    if len(set(lencheck(matrix1)[x]))<=1:
        print(matrix1[x]," → ",transpose(matrix1[x]))
    else:
        print(matrix1[x]," → ",ValueError)
print(" ")
print("row_sums")
for x in range(0,len(lencheck(matrix2))):
    if len(set(lencheck(matrix2)[x]))<=1:
        print(matrix2[x]," → ",row_sums(matrix2[x]))
    else:
        print(matrix2[x]," → ",ValueError)
print(" ")
print("col_sums")
for x in range(0,len(lencheck(matrix2))):
    if len(set(lencheck(matrix2)[x]))<=1:
        print(matrix2[x]," → ",row_sums(transpose(matrix2[x])))
    else:
        print(matrix2[x]," → ",ValueError)
#запуск      py .\src\lab02\matrix.py