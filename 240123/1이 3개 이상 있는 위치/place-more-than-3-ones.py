n = int(input())

matrix = [list(map(int, input().split())) for i in range(n)]

'''
아래 -> x + 1
위 -> x - 1
'''
#     상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y <n

result_value = 0
for i in range(n):
    for j in range(n):
        cnt_value = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if not in_range(nx, ny):
                continue
            if matrix[nx][ny] == 1:
                cnt_value += 1
        if cnt_value >= 3:
            result_value += 1
print(result_value)