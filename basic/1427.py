#1427

n = str(input())
lst = []

for i in range(len(n)):
    lst.append(int(n[i]))

lst.sort(reverse=True)

print(*lst,sep="")