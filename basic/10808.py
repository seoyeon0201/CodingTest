#10808

s = str(input())

n = [0] * 26

for i in range(len(s)):
    n[ord(s[i])-97] += 1

print(*n)