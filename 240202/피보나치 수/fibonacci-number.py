'''
1) Tabulation: for 
2) Memoization:  Recursive + Caching
'''
'''
n = int(input())

memo = [ -1 for _ in range(n + 1) ] 

def fibo(n):
    # 이미 fibo(n)을 구해본 적이 있다면
    # 바로 반
    if memo[n] != -1:
        return memo[n]
    
    # fibo(n)을 계산해본 적이 없다면
    # 계산 결과를 memo[n]에 담아준 뒤
    if n <= 2:
        memo[n] = 1
    else:
        memo[n] = fibo(n-1) + fibo(n-2)
    
    # memo[n]을 반환
    return memo[n]

print(fibo(n))
'''
n = int(input())
f_list = [1, 1]

for i in range(2, n + 1):
    new_num = f_list[i - 1] * f_list[i - 2]
    f_list.append(new_num)

print(f_list[n - 1])