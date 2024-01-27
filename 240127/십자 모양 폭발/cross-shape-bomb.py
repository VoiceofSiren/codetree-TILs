n = int(input())
square = [list(map(int, input().split())) for _ in range(n)]
r, c = tuple(map(int, input().split()))
r, c = r - 1, c - 1

selected_num = square[r][c]
loop_count = selected_num - 1
# print(f'selected_num: square[{r}][{c}] = {square[r][c]}')

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def explode(r, c, square):
    for i in range(r - loop_count, r + loop_count + 1):
        if not in_range(i, 0):
            continue
        else:
            square[i][c] = 0
    for j in range(c - loop_count, c + loop_count + 1):
        if not in_range(0, j):
            continue
        else:
            square[r][j] = 0
    # print('--- explode ---')
    # for row in square:
    #     for element in row:
    #         print(element, end=' ')
    #     print()
    # print('---------------')
            

def count_zeros(column):
    count_value = 0
    for c in column:
        if c == 0:
            count_value += 1
    return count_value

def get_index_of_first_zero(column):
    index = 0
    for c in column:
        if c == 0:
            return index
        else:
            index += 1
    return index

def get_index_of_last_zero(column):
    index = n - 1
    for index in range(n-1, -1, -1):
        if column[index] == 0:
            break
    return index

def fall_down(r, c, square):
    for i in range(n):
        column = []
        for j in range(n):
            column.append(square[j][i])
        # print('fall_down1:', column)

        zeros = count_zeros(column)
        si = get_index_of_first_zero(column)
        ei = get_index_of_last_zero(column)
        # print(f'zeros = {zeros}, si = {si}, ei = {ei}')
        if zeros > 0:
            if zeros == 1:
                for j in range(si, 0, -1):
                    column[j] = column[j - zeros]
                column[0] = 0
            else:
                for j in range(ei, si, -1):
                    column[j] = column[j - zeros]
                for j in range(zeros):
                    column[j] = 0
        
        # print('fall_down2:', column)
        for j in range(n):
            square[j][i] = column[j]

explode(r, c, square)
fall_down(r, c, square)

for i in range(n):
    for j in range(n):
        print(square[i][j], end=' ')
    print()