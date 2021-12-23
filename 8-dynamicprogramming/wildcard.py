##미완성 다시 해야됨....

C = int(input())


for _ in range(C):
    W = str(input())

    N = int(input())

    string_list = []
    for _ in range(N):
        string_list.append(str(input()))
    
    memo = [['x' for _ in range(101)] for _ in range(101)]
    
    def match(w_idx, s_idx,W,S):
        init_w_idx = w_idx
        init_s_idx = s_idx
        if memo[w_idx][s_idx] != 'x':
            return memo[w_idx][s_idx]

        # *를 만나거나 끝나기 전까지 계속 pos 증가
        while w_idx < len(W) and s_idx < len(S) and (W[w_idx] == '?' or W[w_idx] == S[s_idx]):
            w_idx += 1
            s_idx += 1 
        #print(f"w:{w},s:{s},pos:{pos}")
        
        # 만약 패턴의 끝에 도달했다면 모든 문자열을 consume했는 지 확인.
        if w_idx == len(W):
            if s == len(S):
                memo[init_w_idx][init_s_idx] = True
                return memo[init_w_idx][init_s_idx]
 

        #만약 현재 패턴 '*'를 만나서 그만뒀을 경우.
        if W[w_idx] == '*':
            for next in range(len(s[s_idx:]) + 1):
                #print(f"w:{w},s:{s},w[pos+1:]:{w[pos+1:]}s[pos+next:]:{s[pos+next:]}")
                if match(w_idx+1, s_idx+next, W, S):
                    memo[init_w_idx][init_s_idx] = True
                    return True

        memo[init_w_idx][init_s_idx] = False
        return memo[init_w_idx][init_s_idx]


    for s in string_list:
        #print("-"*10)
        if match(0,0,W,s):
            print(s)