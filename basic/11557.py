#백준 11557

T = int(input())

for _ in range(T):
    school = ""
    number = 0
    N = int(input())
    for _ in range(N):
        n, m = input().split()
        m = int(m)
        if (number == 0):
            school = n
            number = m
        elif (number < m):
            school = n
            number = m
            
    print(school)