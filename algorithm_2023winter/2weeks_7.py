# 2주차 7번 주사위 게임

n = int(input())

dices = [[int(x) for x in input().split()] for _ in range(n)]

most = 0
for dice in dices:
    money = 0
    dice.sort()
    if (dice[0] == dice[1] == dice[2]):
        money += 10000+(dice[0]*1000)
    elif (dice[0] == dice[1] or dice[1] == dice[2]):
        money += 1000+(dice[1]*100)
    else:
        money += dice[2]
    if (money > most):
        most = money
print(most)