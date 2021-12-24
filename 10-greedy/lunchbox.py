C = int(input())

for _ in range(C):
    lunchbox_num = int(input())

    hit_time_list = list(map(int,input().split()))
    eat_time_list = list(map(int,input().split()))

    hit_eat_time_list = list(zip(hit_time_list,eat_time_list))


    def heat(hit_time_list,eat_time_list):
        hit_eat_time_list = list(zip(hit_time_list,eat_time_list))

        sorted(hit_eat_time_list,key=lambda x:x[1],reverse=True)

        ret = 0

        begin_eating_time = 0

        for hit_time, eat_time in hit_eat_time_list:
            begin_eating_time += hit_time #먹기 시작하는 시간은 이때까지 데운 시간에 의존한다.
            ret = max(ret, begin_eating_time + eat_time) # 현재까지 먹고 있는 사람 vs 지금 데우고 먹는 사람
        
        return ret
    
    print(heat(hit_time_list,eat_time_list))
