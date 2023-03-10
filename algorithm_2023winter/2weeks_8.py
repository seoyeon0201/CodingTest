# 2주차 8번 점수계산

n = int(input())

OX = [int(x) for x in input().split()]

#front가 앞의 채점 결과를 알려줌
score = 0
front = 0
for ox in OX:
    if (ox == 1):
        front += 1
    else:
        front = 0
    score += front
print(score)