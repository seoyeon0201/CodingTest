# 3주차 3번 두 리스트 합치기

n1 = int(input())
list1 = [int(x) for x in input().split()]
n2 = int(input())
list2 = [int(x) for x in input().split()]

result = []

i = 0
j = 0
while True:
    if (i < n1 and j < n2):
        if (list1[i] <= list2[j]):
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    else:
        if (i < n1):
            for m in range(i, n1):
                result.append(list1[m])
            break
        else:
            for n in range(j, n2):
                result.append(list2[n])
            break

for k in range(n1+n2):
    print(result[k], end=" ")