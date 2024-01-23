#x, y = 10, 20

#dir_num = int(input())

# 1. x, y가 이동하는 경우의 코드
'''
if dir_num == 0:    # 동쪽
    x += 1
elif dir_num == 1:  # 남쪽
    y -= 1
elif dir_num == 2:  # 서쪽
    x -= 1
else:               # 북쪽
    y += 1
'''

# 2. x, y에서 dir_num 방향으로 이동한 위치가 어디인지 구하는 코드
'''
if dir_num == 0:
    nx = x + 1
    ny = y
elif dir_num == 1:
    nx = x
    ny = y - 1
elif dir_num == 2:
    nx = x - 1
    ny = y
else:
    nx = x
    ny = y + 1
'''

# 3. dx dy 테크닉
'''
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
'''
'''
if dir_num == 0:
    nx = x + dx[0]
    ny = y + dx[0]
elif dir_num == 1:
    nx = x + dx[1]
    ny = y + dy[1]
elif dir_num == 2:
    nx = x + dx[2]
    ny = y + dy[2]
elif dir_num == 3:
    nx = x + dx[3]
    ny = y + dx[3]
'''
'''
nx = x + dx[dir_num]
ny = y + dy[dir_num]
'''



n = int(input())

def getInput():
    inputList = input().split()
    direction, distance = inputList[0], int(inputList[1])
    return direction, distance

x, y = 0, 0


dirDict = {
    'W': 0,
    'S': 1,
    'N': 2,
    'E': 3
}
#      W  S  N  E
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
for i in range(n):
    direction, distance = getInput()
    for j in range(distance):
        x = x + dx[dirDict[direction]]
        y = y + dy[dirDict[direction]]

print(x, y)