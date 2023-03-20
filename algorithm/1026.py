# 1_2 보물

n = int(input())

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

A.sort(reverse=True)

sum = 0
for i in range(n):
    sum += A[n-i-1]*max(B)
    B.remove(max(B))

print(sum)
