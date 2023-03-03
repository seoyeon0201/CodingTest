# 1_1 시험 감독 <백준 #13458 => Greedy Algorithm 사용

n = int(input())
people = [int(x) for x in input().split()]
admin = [int(x) for x in input().split()]

cnt = 0
for i in range(n):
    if (people[i] <= admin[0]):
        cnt += 1
        continue
    else:
        cnt += 1
        n_people = people[i] - admin[0]
        if (n_people%admin[1] == 0):
            cnt += n_people//admin[1]
        else:
            cnt += n_people//admin[1] + 1
print(cnt)
