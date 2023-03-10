# 3주차 1번 회문 문자열 검사

n = int(input())

words = [[x.upper() for x in input()] for _ in range(n)]

for word in words:
    check = 0   #회문문자열일 경우 0, 아닐 경우 1
    for i in range(len(word)//2):
        if (word[i] == word[len(word)-i-1]):
            pass
        else:
            check = 1
    if (check == 0):
        print("YES")
    else:
        print("NO")