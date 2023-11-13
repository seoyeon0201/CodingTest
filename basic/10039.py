#10039

lst = []
sum = 0

for _ in range(5):
    n = int(input())
    lst.append(n)

for num in lst:
    if (num <= 40):
        sum += 40
    else:
        sum += num

print(sum//5)