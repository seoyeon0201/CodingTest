#14503 로봇청소기

N,M = map(int, input().split())

r,c,d = map(int, input().split())

rooms = [[x for x in map(int, input().split())] for _ in range(N)]
# dp = [[[True] for _ in range(M)] for _ in range(N)]
# for i in range(N):
#     for j in range(M):
#         if rooms[i][j] == 0:
#             dp[i][j] = "empty,0"
#         elif rooms[i][j] == 1:
#             dp[i][j] = "wall,1"
#         else:
#             dp[i][j] = "full,2"

current = [r, c, d]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
#재귀함수 사용
def current_pos(r,c,d,clean_n):
    if rooms[r][c] == 0:                                #1. 현재 칸이 청소되지 않은 경우 현재 칸 청소
        rooms[r][c] = 2
        clean_n += 1  # 전체 청소한 칸 수
    empty_n = find_empty(r,c)  #주변에 비어있는 칸 수
    if empty_n == 0:    #case2
        back_lst = can_back(r,c,d)  #벽 존재하면 back_lst = [d]만 존재
        if len(back_lst) == 1:                          #2_2. back_lst가 1일 경우 = 후진할 수 없는 경우
            print(clean_n)
            return
        else:                                           #2_1. 후진할 수 있으면 후진하고 1번으로
            current_pos(back_lst[0], back_lst[1], back_lst[2], clean_n)
    else:   #case3
        rotate_lst = find_rotate_90(r,c,d)          #3_1. find_rotate_90: 90도씩 돌려서 앞에 빈 칸 있으면 (x,y,d)리턴
        forward_lst = can_forward(rotate_lst[0], rotate_lst[1], rotate_lst[2])  #3_2.
        current_pos(forward_lst[0], forward_lst[1], forward_lst[2], clean_n)    #3_3

# 현재 칸 청소 함수
def find_empty(x, y):
    cnt = 0 #해당 좌표 주변의 빈 칸 수
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if rooms[nx][ny] == 0:
            cnt += 1
    return cnt

#d방향 후방의 칸에 벽만 아닌 것이 존재하면 xyd_lst에 [x,y,d] 존재. 벽일 경우 [d]만 존재
def can_back(x,y,d):
    xyd_lst = [] #x,y,d까지
    if d==0:
        if rooms[x+1][y] != 1:
            xyd_lst.append(x+1)
            xyd_lst.append(y)
    elif d==1:
        if rooms[x][y-1] != 1:
            xyd_lst.append(x)
            xyd_lst.append(y-1)
    elif d==2:
        if rooms[x-1][y] != 1:
            xyd_lst.append(x-1)
            xyd_lst.append(y)
    elif d==3:
        if rooms[x][y+1] != 1:
            xyd_lst.append(x)
            xyd_lst.append(y+1)
    xyd_lst.append(d)
    return xyd_lst

#find_rotate_90: 90도씩 돌려서 앞에 빈 칸 있으면 (x,y,d)리턴. 빈 칸 있을 때까지 반복
def find_rotate_90(x,y,d):
    xyd_lst = []    #x,y,d까지
    check = 0
    # 90도 돌기
    while check==0:
        if d==0:
            d = 3  # 북->서
            if rooms[x][y-1] == 0:
                check = 1
        elif d==1:
            d = 0  # 동->북
            if rooms[x-1][y] == 0:
                check = 1
        elif d==2:
            d = 1  # 남->동
            if rooms[x][y+1] == 0:
                check = 1
        elif d==3:
            d = 2  # 서->남
            if rooms[x+1][y] == 0:
                check = 1
    xyd_lst.append(x)
    xyd_lst.append(y)
    xyd_lst.append(d)
    return xyd_lst

def can_forward(x,y,d):
    xyd_lst = []
    if d==0:
        x-=1
    elif d==1:
        y+=1
    elif d==2:
        x+=1
    elif d==3:
        y-=1
    xyd_lst.append(x)
    xyd_lst.append(y)
    xyd_lst.append(d)
    return xyd_lst


#<main함수>
current_pos(r,c,d,0)    ##결과는 current_pos 안에서 출력