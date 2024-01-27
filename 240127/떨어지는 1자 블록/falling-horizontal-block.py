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
        if block[j] == 1 and matrix[i + 1][j] == 1:
            continue
        else:
            flag += 1
    # print('flage =', flag)
    return flag == n

i = -1
while True:
    if ok_to_move(i):
        i += 1
        if i + 1 >= n:
            for j in range(n):
                if block[j] == 1:
                    matrix[i][j] = 1
            break
    else:
        for j in range(n):
            if block[j] == 1:
                matrix[i][j] = 1
        break




#####################################################################################################
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()





'''
Traceback (most recent call last):
File "/tmp/Main.py", line 30, in <module>
if ok_to_move(i):
^^^^^^^^^^^^^
File "/tmp/Main.py", line 21, in ok_to_move
if block[j] == 1 and matrix[i + 1][j] == 1:
^^^^^^^^^^^^^
IndexError: list index out of range
'''