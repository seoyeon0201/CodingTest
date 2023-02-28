#2주차 3번 정다면체

# n, m 입력
n, m = map(int, input().split())

# 각각 나올 수 있는 눈 list 생성 
n_lst = [int(x) for x in range(1,n+1)]
m_lst = [int(x) for x in range(1,m+1)]

# 가능한 눈의 합 list sum 생성
sum = []
for i in range(n):
    for j in range(m):
        sum.append(n_lst[i]+m_lst[j])

# 확률이 높은 수 찾기:count
sum_set = list(set(sum))    #중복제거한 값 list
most = []    #기장 많이 count된 수 list
cnt = 0     #가장 많이 count된 count
for k in sum_set:
    if (sum.count(k)>cnt):
        most = [k]
        cnt = sum.count(k)
    elif (sum.count(k) == cnt):
        most.append(k)
print(*most)