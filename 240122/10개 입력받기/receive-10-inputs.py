intArr = list(map(int, input().split()))
resultArr = []
for x in intArr:
    if x != 0:
        resultArr.append(x)
    else:
        break
# print(resultArr)
print(f'{sum(resultArr)} {sum(resultArr)/len(resultArr):.1f}')