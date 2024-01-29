import functools

n, m = tuple(map(int, input().split()))
num_list = list(map(int, input().split()))
visited = [
    False for _ in range(n)
]
answer = 0

def operate_xor():
    value = 0
    for i in range(n):
        if visited[i]:
            value ^= num_list[i]
    return value

def find_max_xor(current_index, count_value):
    global answer
    
    if count_value == m:
        answer = max(answer, operate_xor())
        return
    
    if current_index == n:
        return
    
    # current_index에 있는 숫자를 선택하지 않은 경우
    find_max_xor(current_index + 1, count_value)
    
    # current_index에 있는 숫자를 선택한 경우
    visited[current_index] = True
    find_max_xor(current_index + 1, count_value + 1)
    visited[current_index] = False

find_max_xor(0, 0)

print(answer)