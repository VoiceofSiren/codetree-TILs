n, m, k = tuple(map(int, input().split()))
k = k - 1

matrix = [
    list(map(int, input().split()))
    for _ in range(n)
]

block = []
for i in range(n):
    if k <= i < k + m:
        block.append(1)
    else:
        block.append(0)

#####################################################################################################

def ok_to_move(i):
    flag = 0
    for j in range(n):
        if block[j] == 1 and matrix[i][j] == 1:
            continue
        else:
            flag += 1
    return flag == n

i = 0
while True:
    if ok_to_move(i):
        i += 1
    else:
        for j in range(n):
            if matrix[i][j] == 0 and block[j] == 1:
                matrix[i][j] = block[j]
        break




#####################################################################################################
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()






# print('block')
# for b in block:
#     print(b, end= ' ')
# print()

# print('matrix')
# for row in matrix:
#     for element in row:
#         print(element, end=' ')
#     print()