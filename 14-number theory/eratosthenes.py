

def eratosthenes(N):
    eratosthenes_list = [True for _ in range(N+1)]

    eratosthenes_list[0] = eratosthenes_list[1] = False

    sqrtN = int(N**(1/2))
    for i in range(2,sqrtN+1):

        if eratosthenes_list[i]:
            for j in range(i*i,N+1,i):
                eratosthenes_list[j] = False
        
    
    return eratosthenes_list


if __name__ == '__main__':
    N = int(input())

    era_list = eratosthenes(N)

    for i , v in enumerate(era_list):
        if i==0: continue
    
        print(f"i : {i} , v : {v}")
