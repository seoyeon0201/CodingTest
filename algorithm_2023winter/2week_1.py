# 졸작코테_2주차 1번문제 K번째 큰 수

n, k = map(int, input().split())

lst = [int(x) for x in map(int, input().split())]
lst = list(set(lst))
sum = []
for i in range(n-3):
    for j in range(i+1, n-2):
        for p in range(j+1, n-1):
            sum.append(lst[i]+lst[j]+lst[p])
sum.sort(reverse=True)
print(sum[k-1])
