n, t = list(map(int, input().split()))

c_belt = [list(map(int, input().split())) for _ in range(2)]

time = 0
while time < t:
    
    temp1 = c_belt[0][n-1]
    temp2 = c_belt[1][n-1]
    for i in range(2):
        for j in range(n-1, 0, -1):
            c_belt[i][j] = c_belt[i][j-1]
        
    c_belt[0][0] = temp2
    c_belt[1][0] = temp1

    time += 1

for i in range(2):
    for j in range(n):
        print(c_belt[i][j], end=' ')
    print()