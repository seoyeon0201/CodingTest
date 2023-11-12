#9506

check= True

while (check):
    lst = []
    sum = 0
    n = int(input())

    if (n == -1):
        check = False
    else:
        for i in range(1,n):
            if (n%i==0):
                lst.append(i)

        for j in range(len(lst)):
            sum += lst[j]
        
        if (sum == n):
            lst1 = []
            for l in range(len(lst)):
                lst1.append(str(lst[l]))
            print(n,"=",' + '.join(lst1))
        else:
            print(n, "is NOT perfect.")