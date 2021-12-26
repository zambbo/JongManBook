L = 2000000000

def ratio(game, wons):
    return int((wons*100)/game)


def neededGames(game, current_wons):

    if ratio(game,current_wons) == ratio(game+L,current_wons+L):
        return -1
    
    lo = 0
    hi = L

    for _ in range(100):
        mid = int((lo+hi)/2)

        if ratio(game+mid,current_wons+mid) > ratio(game,current_wons):
            hi = mid
        else:
            lo = mid
    
    return hi



if __name__ == '__main__':
    C = int(input())

    for _ in range(C):
        N,M = tuple(map(int,input().split()))

        print(neededGames(N, M))