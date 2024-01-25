n, m = list(map(int, input().split()))
square = [list(map(int, input().split())) for _ in range(n)]
loop_count = n - m + 1

def in_range(x, y):
    return 0 <= x <= n-1 and 0 <= y <= n-1

def horizontal_search(j, square):
    count_value = 1
    for i in range(n):
        if square[i][j] == square[i][j+1]:
            count_value += 1
            #print(f'h: x={i}, y={j}, cv={count_value}')
            if count_value == m:
                return (i, j)
        else:
            count_value = 1
    return (-1, -1)

def vertical_search(i, square):
    count_value = 1
    for j in range(n):
        if square[i][j] == square[i+1][j]:
            count_value += 1
            #print(f'v: x={i}, y={j}, cv={count_value}')
            if count_value == m:
                return (i, j)
        else:
            count_value = 1
    return (-1, -1)

answer_arr = []
answer = 0
for i in range(loop_count): # i = 0, 1
    answer_arr.append(vertical_search(i, square))
    temp_set = set()
    for pairs in answer_arr:
        temp_set.add(pairs[1])
    answer += len(temp_set)/4


for j in range(loop_count): # j = 0, 1
    answer_arr.append(horizontal_search(j, square))
    temp_set = set()
    for pairs in answer_arr:
        temp_set.add(pairs[0])
    answer += len(temp_set)/4

print(int(answer))