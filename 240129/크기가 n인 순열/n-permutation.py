n = int(input())
arr = []
visited = [ 0 for _ in range(n)]

def print_arr():
    for element in arr:
        print(element + 1, end=' ')
    print()

def make_permutations(current_num):
    if current_num == n:
        print_arr()
        return
    
    for i in range(n):
        if visited[i] == 1:
            continue
        arr.append(i)
        visited[i] = 1
        make_permutations(current_num + 1)
        visited[arr.pop()] = 0

make_permutations(0)