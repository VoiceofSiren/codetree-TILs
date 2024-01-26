n, t = tuple(map(int, input().split()))
c_belt = [list(map(int, input().split())) for i in range(3)]


def rotate(c_belt):
    temp_list = []
    for i in range(3):
        temp_list.append(c_belt[i][n-1])
    for i in range(3):
        for j in range(n-1, 0, -1):
            c_belt[i][j] = c_belt[i][j-1]
        c_belt[i][0] = temp_list[(i + 2) % 3]

for _ in range(t):
    rotate(c_belt)

for row in c_belt:
    for element in row:
        print(element, end=' ')
    print()