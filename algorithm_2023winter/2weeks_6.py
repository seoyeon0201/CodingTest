# 2주차 6번 뒤집은 소수 

def reverse(x):
    number = []
    for i in str(x):
        number.append(int(i))
    for j in range(len(number)//2):
        number[j], number[-j-1] = number[-j-1], number[j]
    while (number[0] == 0):
        del number[0]
    reverse_n = 0
    for k in range(len(number)):
        reverse_n += number[-k] * 10**(len(number)-k-1)
    return reverse_n


def isPrime(x):
    ck = True
    if (x <= 1):
        pass
    else:
        for i in range(2, x):
            if (x % i == 0):  # 소수 아님
                ck = False
        if (ck == True):
            return True


n = int(input())
n_list = [int(x) for x in input().split()]
result = []

for t in n_list:
    reverse_number = reverse(t)
    if (isPrime(reverse_number) == True):
        result.append(reverse_number)
print(*result)
