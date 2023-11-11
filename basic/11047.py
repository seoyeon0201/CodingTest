# 백준 #11047 동전0 => Greedy Algorithm
# 높은 가치의 동전들은 모두 낮은 가치의 동전의 배수이므로 그리디 성립

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)  # 높은 가치의 동전 먼저 사용

result = 0  #총 coins의 갯수
for coin in coins:
    cnt = 0
    if (k >= coin):
        cnt = k//coin   #해당 coin의 갯수
        k = k - cnt*coin
        result += cnt   

print(result)