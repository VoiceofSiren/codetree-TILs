n = int(input())
answer = 0
arr = []


def is_beautiful():
    i = 0
    while i < n:
        if i + arr[i] - 1 >= n:
            return False

        for j in range(i, i + arr[i]):
            if arr[j] != arr[i]:
                return False
        i += arr[i]
        
    return True


def count_beautiful_numbers(cnt):
    global answer
    
    if cnt == n:
        if is_beautiful():
            answer += 1
        return
	
    for i in range(1, 5):
        arr.append(i)
        count_beautiful_numbers(cnt + 1)
        arr.pop()


count_beautiful_numbers(0)
print(answer)