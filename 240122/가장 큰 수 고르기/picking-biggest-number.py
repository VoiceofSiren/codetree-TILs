import sys

max_val = -sys.maxsize

inputList = list(map(int, input().split()))

for element in inputList:
    if element > max_val:
        max_val = element
print(max_val)