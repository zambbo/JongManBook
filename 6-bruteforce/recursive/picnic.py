C = int(input())




for _ in range(C):
    n, m= map(int,input().split())
    areFriends = [[False]*n for _ in range(n)]
    relations = list(map(int,input().split()))
    taken = [False]*n

    for idx in range(0,len(relations),2):
        areFriends[relations[idx]][relations[idx+1]] = True
        areFriends[relations[idx+1]][relations[idx]] = True

    def countParings(taken):
        firstFree = -1

        for idx,t in enumerate(taken):
            if t == False:
                firstFree = idx
                break

        if firstFree == -1:
            return 1

        ret = 0

        for idx in range(firstFree+1,n):
            if areFriends[firstFree][idx] and (not taken[firstFree]) and (not taken[idx]):
                taken[idx], taken[firstFree] = True, True
                ret += countParings(taken)
                taken[idx], taken[firstFree] = False, False
        return ret

    print(countParings(taken))
    



