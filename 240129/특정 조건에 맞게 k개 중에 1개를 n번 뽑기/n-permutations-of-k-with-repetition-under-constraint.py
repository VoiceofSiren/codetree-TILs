k, n = tuple(map(int, input().split()))
arr = []

def print_num(arr):
    for element in arr:
        print(element, end=' ')
    print()

def in_range(x):
    return 0 <= x < n

def count_num(num_count, num, arr):
    if num_count < 2:
        return True 
    else:
        if arr[num_count - 2] == arr[num_count - 1] and arr[num_count - 1] == num:
            return False
        else:
            return True


def make_permutations(num_count):
    
    if num_count == n:
        print_num(arr)
        return

    for i in range(1, k + 1):
        if count_num(num_count, i, arr):
            arr.append(i)
            make_permutations(num_count + 1)
            arr.pop()
    return

make_permutations(0)