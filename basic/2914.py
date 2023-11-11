#2914 저작권

A, I = map(int, input().split())

if (A==1):
    print(I)
else:
    print(A*(I-1)+1)    # 적어도이르모 I가 아닌 I-1로 계산한 후 +1