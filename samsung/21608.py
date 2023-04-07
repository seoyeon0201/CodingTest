#21608 상어 초등학교

n = int(input())

table = [[x for x in map(int, input().split())] for _ in range(n*n)]

#dp와 같이 이중리스트 만들 때 * 쓰지말고 for _ in range () 사용
dp = [[0] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def favorite(list, dp):
    max = 0
    max_lst = [[0 for _ in range(n)]for _ in range(n)]
    favorite_lst = []
    #dp 확인해 max_lst 작성
    for i in range(n):
        for j in range(n):
            if dp[i][j] == 0:
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if (0<=nx<n and 0<=ny<n):
                        if dp[nx][ny] > 0:
                            if dp[nx][ny] in list:
                                max_lst[i][j] += 1
    for i in range(n):
        for j in range(n):
            if max_lst[i][j] > max:
                max = max_lst[i][j]
                favorite_lst = []
                favorite_lst.append([i,j])
            elif max_lst[i][j] == max:
                favorite_lst.append([i, j])

    return favorite_lst

def empty(list, favorite_lst):
    max = 0
    max_lst = [[0 for _ in range (n)] for _ in range(n)]
    empty_lst = []
    for i in range(len(favorite_lst)):
        x = favorite_lst[i][0]
        y = favorite_lst[i][1]
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if (0<=nx<n and 0<=ny<n):
                if dp[nx][ny]==0:
                    max_lst[x][y] += 1

    for i in range(n):
        for j in range(n):
            if max_lst[i][j] > max:
                max = max_lst[i][j]
                empty_lst = []
                empty_lst.append([i, j])
            elif max_lst[i][j] == max:
                empty_lst.append([i, j])

    return empty_lst

def low(empty_lst):
    result = []
    #오름차순 정렬
    empty_lst.sort(key=lambda x:x[0])
    same_lst = [empty_lst[0]]
    for i in range(len(empty_lst)):
        if empty_lst[i][0] == empty_lst[0][0]:
            same_lst.append(empty_lst[i])
    same_lst.sort(key=lambda x:x[1])
    result = same_lst[0]

    return result


#자리 정하기
for k in range(n*n):
    favorite_lst = favorite(table[k],dp)
    if len(favorite_lst) == 1:
        dp[favorite_lst[0][0]][favorite_lst[0][1]] = table[k][0]
    else:
        empty_lst = empty(table[k], favorite_lst)
        if len(empty_lst) == 1:
            dp[empty_lst[0][0]][empty_lst[0][1]] = table[k][0]
        else:
            result = low(empty_lst)
            dp[result[0]][result[1]] = table[k][0]

table.sort()


#만족도
sum = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]
            if (0<=nx<n and 0<=ny<n):
                if (dp[nx][ny] in table[dp[i][j]-1]):
                    cnt+=1
        if cnt == 0:
            continue
        elif cnt == 1:
            sum += 1
        elif cnt == 2:
            sum += 10
        elif cnt == 3:
            sum += 100
        elif cnt == 4:
            sum += 1000
print(sum)