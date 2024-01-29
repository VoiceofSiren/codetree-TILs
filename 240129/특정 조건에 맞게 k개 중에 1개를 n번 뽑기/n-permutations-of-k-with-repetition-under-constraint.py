k, n = tuple(map(int, input().split()))
arr = []

def print_num(arr):
    for element in arr:
        print(element, end=' ')
    print()

def in_range(x):
    return 0 <= x < n

def count_num(n, num, arr):
    if not in_range(n - 1):
        return True
    if not in_range(n - 2):
        return True
    if arr[n -2] == arr[n - 1] and arr[n - 1] == num:
        return False
    else:
        return True


def make_permutations(num_count):
    
    if num_count == n:
        print_num(arr)
        return

    for i in range(1, k + 1):
        if count_num(n,i, arr):
            arr.append(i)
            make_permutations(num_count + 1)
            arr.pop()
    return

make_permutations(0)