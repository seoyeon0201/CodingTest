#백준 1065

x = int(input())

def d(n):
    cnt = 0

    for i in range(1, n+1):
        lst = list()
        for j in str(i):    #i가 123일 때, j는 1,2,3
            lst.append(int(j)) 

        if (len(lst) == 1):
            cnt += 1
        elif (len(lst) == 2):
            cnt += 1
        else:
            if ((lst[0]+lst[2])/2 == lst[1]):
                cnt += 1
    return (cnt)

print(d(x))
