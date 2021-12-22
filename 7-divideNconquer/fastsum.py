

def fastSum(n):
    if n == 1: return 1
    if n%2 == 1: return n + fastSum(n-1)
    else:
        return (n//2)**2 + 2*fastSum(n//2)


if __name__ == '__main__':
    N = int(input())
    print(fastSum(N))