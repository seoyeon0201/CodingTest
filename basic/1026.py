#1026

sum = 0

n = int(input())

a = input().split()
b = input().split()

for i in range(n):
    a[i] = int(a[i])
    b[i] = int(b[i])

a.sort()
b.sort(reverse=True)

for j in range(n):
    sum += a[j]*b[j]
print(sum)