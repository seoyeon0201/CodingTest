#백준 10886
n = int(input())

sum = 0

for _ in range(n):
    m = int(input())
    if (m==0):  #안귀여움
        sum -= 1
    else:   #귀여움
        sum += 1

if (sum>0):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
