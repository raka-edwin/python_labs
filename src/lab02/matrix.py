def transpose(mat):
    if len(mat)==0:
        return []
    if len(set(lencheck(mat)))<=1:
        m=len(mat)
        n=len(mat[0])
        mat2=[[0 for i in range(m)]for i in range(n)]
        for x in range(0,m):
            for y in range(0,n):
                mat2[y][x]=mat[x][y]
        return mat2
    else:
        return ValueError

def row_sums(mat):
    if mat==ValueError or len(set(lencheck(mat)))>1:
        return ValueError
    if len(set(lencheck(mat)))<=1 and mat!=ValueError:
        m=len(mat)
        matrix_row_sum=[[]for i in range(m)]
        for i in range(0,m):
            matrix_row_sum[i].append(sum(mat[i]))
        return matrix_row_sum

def lencheck(mat):
    a=[]
    for x in range(0,len(mat)):
        a.append(len(mat[x]))
    return a

matrix1=[[[1,2,3]],[[1],[2],[3]],[[1,2],[3,4]],[],[[1,2],[3]]]
matrix2=[[[1,2,3],[4,5,6]],[[-1,1],[10,-10]],[[0,0],[0,0]],[[1,2],[3]]]

print("transpose")
for x in range(0,len(lencheck(matrix1))):
    print(matrix1[x]," → ",transpose(matrix1[x]))

print(" ")
print("row_sums")
for x in range(0,len(lencheck(matrix2))):
    print(matrix2[x]," → ",row_sums(matrix2[x]))

print(" ")
print("col_sums")
for x in range(0,len(lencheck(matrix2))):
    print(matrix2[x]," → ",row_sums(transpose(matrix2[x])))

#запуск      py .\src\lab02\matrix.py