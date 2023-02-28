# 2주차 2번 대표값

n = int(input())

n_lst = [int(x) for x in input().split()]

# 평균
sum = 0
for i in range(n):
    sum += n_lst[i]
avg = round(sum/n)  #round: 소수점 제한

# 평균과의 차이
gap = abs(avg-n_lst[0])
index = 0
for j in range(1, n):
    if (abs(avg-n_lst[j]) < gap):   #gap보다 작을 경우, 선택
        gap = abs(avg-n_lst[j])
        index = j
    elif (abs(avg-n_lst[j]) == gap):    #gap이 같을 경우, 값이 크고 번호가 빠르도록
        if (n_lst[j] > n_lst[index+1]): #등호 들어가지 않아서 빠른 번호도 성립
            gap = abs(avg-n_lst[j])
            index = j

print(avg, index+1)