

def eratosthenes(N):
    eratosthenes_list = [i for i in range(N+1)]

    eratosthenes_list[0] = eratosthenes_list[1] = -1

    sqrtN = int(N**(1/2))
    for i in range(2,sqrtN+1):
        
        if eratosthenes_list[i] == i:
            for j in range(i*i,N+1,i):
                if eratosthenes_list[j] == j:
                    eratosthenes_list[j] = i
        
    
    return eratosthenes_list

def factor(N):
    eratosthenes_list = eratosthenes(N)
    factor_list = []
    while N > 1:
        factor_list.append(eratosthenes_list[N])
        N //= eratosthenes_list[N]
    
    return factor_list

if __name__ == '__main__':
    N = int(input())

    era_list = eratosthenes(N)

    for i , v in enumerate(era_list):
        if i==0: continue
    
        print(f"i : {i} , v : {v}")
    print(factor(N))