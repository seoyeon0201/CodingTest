# 2주차 4번 자릿수의 합

#digit_sum 함수 생성
def digit_sum(x):
    sum = 0
    for i in str(x):
        i = int(i)
        sum += i
    return sum

#입력
n = int(input())
n_list = [int(x) for x in input().split()]

#비교
highest = digit_sum(n_list[0])
for k in range(1,n):
    if (digit_sum(n_list[k]) > highest):
        highest = n_list[k]
print(highest)