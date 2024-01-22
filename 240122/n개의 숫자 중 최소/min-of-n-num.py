import sys

n = int(input())
inputList = list(map(int, input().split()))

min_value = sys.maxsize

for e in inputList:
    if e < min_value:
        min_value = e

min_count = 0
for e in inputList:
    if e == min_value:
        min_count += 1
print(min_value, min_count)