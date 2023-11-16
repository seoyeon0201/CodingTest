#2476

price = 0

n = int(input())

for _ in range(n):
    a, b, c = map(int, input().split())
    sum = 0
    most = a

    if (a==b==c):
        sum += 10000 + a*1000
    elif (a==b or b==c):
        sum += 1000+b*100
    elif (a==b or a==c):
        sum += 1000+a*100
    else:
        if (b>most):
            most = b
            if (c>most):
                most = c
        else:
            if (c>most):
                most = c
        sum+= most*100
    
    if (sum > price):
        price = sum

print(price)