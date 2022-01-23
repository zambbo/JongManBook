C = int(input())


for _ in range(C):
    N, K = map(int,input().split())

    soldiers = [i for i in range(1,N+1)]

    len = N
    now = 0
    while len > 2:
        #print(len, now)
        del soldiers[now]
        len -= 1
        now += K-1
        now %= len
        

    print(soldiers)

