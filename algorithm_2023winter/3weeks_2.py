# 3주차 2번 숫자만 추출

words = input()

# 숫자 추출
num = ""
for word in str(words):
    if ord(word) >= 49 and ord(word) <= 81:
        num += word

num = int(num)

# 약수 추출
cnt = 0
for i in range(1, num+1):
    if ((num % i) == 0):
        cnt += 1

print(num, cnt, sep="\n")