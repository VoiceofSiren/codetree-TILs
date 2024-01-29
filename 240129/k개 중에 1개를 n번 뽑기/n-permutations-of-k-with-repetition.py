k, n = tuple(map(int, input().split()))
answer = []

def print_answer():
    for element in answer:
        print(element, end=' ')
    print()

def choose(current_index):
    if current_index == n:
        print_answer()
        return
    
    for i in range(k):
        answer.append(i + 1)
        choose(current_index + 1)
        answer.pop()
    
    return

choose(0)