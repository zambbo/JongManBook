

def balance(N, M, P, C):
    balance = N

    for _ in range(int(M)):
        balance *= (1.0 + (P/12)/100)

        balance -= C
    
    return balance

def payment(N, M, P):
    lo = 0
    hi = N * (1.0 + (P/12)/100)

    for _ in range(100):
        mid = (lo + hi) / 2.0

        # 만약 해당 기간에 다 갚을 수 있다면 hi = mid (lo, mid) 구간에서 다시 찾아본다.
        if balance(N,M,P,mid) <= 0:
            hi = mid
        else:
            lo = mid
    
    # 왜 hi냐? lo는 해당 기간안에 다 못갚을 경우 hi 는 갚을 경우 이므로!
    return hi

if __name__ == '__main__':
    N = float(input())
    P = float(input())
    M = float(input())
    print(payment(N, M, P))    