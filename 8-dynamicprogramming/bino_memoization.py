memo = [[-1 for _ in range(30)] for _ in range(30)]



def bino(n, r):
    if r == 0 or n == r: return 1
    if memo[n][r] != -1:
        return memo[n][r]
    memo[n][r] = bino(n-1,r-1) + bino(n-1,r)
    return memo[n][r]


if __name__ == '__main__':
    N = int(input())
    R = int(input())
    print(bino(N,R))