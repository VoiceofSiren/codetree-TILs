x, y = 0, 0


#     N  E  S   W
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

command = input()

commandDict = {
    'L': 3, # -1
    'R': 1,
    'F': 0
}

dir_num = 0
for i in range(len(command)):
    nowCommand = command[i]
    dir_num = (dir_num + commandDict[nowCommand]) % 4
    if nowCommand == 'F':
        x = x + dx[dir_num]
        y = y + dy[dir_num]
print(x, y)