# 3주차 4번 수들의 합

N, M = input().split()
N = int(N)
M = int(M)

array = [int(x) for x in input().split()]

cnt = 0
for i in range(N):      #i와 j는 index(0~(N-1), 0~(N-1)까지 존재)
    for j in range(N):
        sum = 0
        for k in range(i, j+1): #k는 index(0~(N-1))
            sum += array[k]
        if (sum == M):  #직전 for문이 모두 돌아가야 sum이 나타남
            cnt += 1

print("cnt: ", cnt)