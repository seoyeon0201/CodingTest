#23291 어항문제 *예제입력8 제외 모두 성공
from collections import deque

n, k = map(int, input().split())
bowls = list()
bowls.append(deque(list(map(int, input().split()))))    #bowls라는 list에 deque 형식의 list 생성
original_bowls = bowls
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#가장 적은 어항에 1마리씩 추가
def plus_fish(graph):
    minimum = min(graph[0])
    for i in range(len(graph[0])):
        if graph[0][i] == minimum:
            graph[0][i] += 1
    return graph[0]

#가장 왼쪽 어항 쌓기
def popleft(graph):
    pop = graph[0].popleft()
    graph.append(deque([pop]))
    graph[0], graph[1] = graph[1], graph[0]
    return graph


#2개 이상 쌓인 어항을 공중부양시킨 후 90도로 회전해 제일 왼쪽에 붙임
def rotate_90_clockdirection(graph):
    pop0 = graph[0].popleft()
    pop1 = graph[1].popleft()
    graph[0].append(pop1)
    graph[0].append(pop0)

def rotate_90_clockdirection2(graph):
    while (len(graph[0])*len(graph) < len(graph[1])):
        pop1 = graph[0].popleft()   #위층의 맨 왼쪽
        pop2 = graph[0].popleft()   #위층의 왼쪽에서 두번째
        pop3 = graph[1].popleft()    #아래층의 맨 왼쪽
        pop4 = graph[1].popleft()   #아래층의 왼쪽에서 두번째

        graph.append(deque([]))
        graph[1], graph[2] = graph[2], graph[1]

        graph[0].append(pop3)
        graph[0].append(pop1)
        graph[1].append(pop4)
        graph[1].append(pop2)

def fish_number(graph):
    dp = [[0] * len(graph[x]) for x in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            for k in range(4):
                nx = i+dx[k]
                ny = j+dy[k]
                if nx<0 or nx>=len(graph) or ny<0 or ny>=len(graph[nx]):
                    continue
                if (graph[i][j] < graph[nx][ny]) :
                    d = (graph[nx][ny] - graph[i][j]) // 5
                    if d>0 :
                      dp[i][j] += d
                else:
                    d = (graph[i][j] - graph[nx][ny]) // 5
                    if d>0 :
                        dp[i][j] -= d
    for x in range(len(graph)):
        for y in range(len(graph[x])):
            graph[x][y] += dp[x][y]

#바닥에 일렬로 놓기
def put_bowl(graph):
    result = [deque([])]
    for i in range(len(graph[0])):
        for j in range(len(graph)):
            pop = graph[len(graph)-1-j].popleft()
            result[0].append(pop)
    for _ in range(len(graph[len(graph)-1])):
        result[0].append(graph[len(graph)-1].popleft())
    graph = result
    return graph

#공중부양
def rotate_180_clockdirection(graph):
    #n/2개 시계방향으로 180도 회전
    graph.append(deque([]))
    graph[0], graph[1] = graph[1], graph[0]
    for _ in range(len(graph[1])//2):
        pop = graph[1].popleft()
        graph[0].appendleft(pop)

    # #한번 더
    n = len(graph[0]) // 2
    for _ in range(2):
        graph.append(deque([]))
    graph[0], graph[len(graph)-2] = graph[len(graph)-2], graph[0]
    graph[1], graph[len(graph)-1] = graph[len(graph)-1], graph[1]
    for i in range(n):
        graph[1].appendleft(graph[len(graph)-2].popleft())
        graph[0].appendleft(graph[len(graph)-1].popleft())

def get_gap(graph):
    dp = graph[0]
    gap = max(dp)-min(dp)
    return gap

cnt = 0
while True:
    gap = get_gap(bowls)
    if gap <= k:
        print(cnt)
        break
    cnt += 1
    plus_fish(bowls)
    popleft(bowls)
    rotate_90_clockdirection(bowls)
    rotate_90_clockdirection2(bowls)
    fish_number(bowls)
    bowls = put_bowl(bowls)
    rotate_180_clockdirection(bowls)
    fish_number(bowls)
    bowls = put_bowl(bowls)
    gap = get_gap(bowls)