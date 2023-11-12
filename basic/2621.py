#2621 카드게임
#아직 해결 X

lst1 = []   #알파벳
lst2 = []   #숫자

for _ in range(5):
    n, m = input().split()
    lst1.append(n)
    lst2.append(int(m))

color = lst1[0]

check1 = False
for i in range(1,5):
    if (lst1[i] != color):
        break
    if (i==4):
        check1 = True

print(check1)