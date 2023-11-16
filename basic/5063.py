#5063

n = int(input())

for _ in range(n):
    a, b, c = map(int, input().split())

    if (b-a>c):
        print("advertise")
    elif (b-a==c):
        print("does not matter")
    else:
        print("do not advertise")