# 3주차 5번 격자판 최대합

n = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])

large = 0

for i in range(n):
    sum = 0
    for j in range(n):
        sum += matrix[i][j]
    if sum >= large:
        large = sum

for p in range(n):
    sum = 0
    for q in range(n):
        sum += matrix[q][p]
    if sum >= large:
        large = sum

sum = 0
for u in range(n):
    sum += matrix[u][u]
if sum >= large:
    large = sum

print(large)