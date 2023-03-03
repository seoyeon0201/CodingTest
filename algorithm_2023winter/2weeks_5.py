# 2주차 5번 소수(에라토스테네스 체)
# 에라토스테네스 체는 2부터 n까지 존재하는 배열(True)에서 2가 소수일 경우 2의 배수를 모두 제거(False)
#이후 수가 증가하면서 반복되는데 이전에 삭제되지 않은 수는 소수

n = int(input())

#0과 1은 소수가 아니고 2는 반드시 소수
numbers = [False, False] + [True]*(n-1)
prime = []

for i in range(2, n+1):
    if numbers[i]:  # True일 경우(즉 소수일 경우) 아래 코드 실행
        prime.append(i)  # prime number가 됨
        for j in range(i*2, n+1, i):    #prime number의 배수는 모두 False(소수 아님)
            numbers[j] = False
print(len(prime))
