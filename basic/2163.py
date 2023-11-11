#2163 초콜릿 자르기

N, M = map(int, input().split())


cnt = 0

if (N==1 or M==1):  #N 또는 M이 1인 경우
    if (N==1 and M==1):
        print(0)
    elif (N==1):
        print(M-1)
    elif (M==1):
        print(N-1)
else:   #더 큰 수를 먼저 자르는 것이 최소로 자르는 방법
    if(N>=M):
        cnt += N-1
        cnt += N * (M-1)
    else:
        cnt += M-1
        cnt += M * (N-1)
    print(cnt)