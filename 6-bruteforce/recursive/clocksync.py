C = int(input())

switches = ["***.............",
"...*...*.*.*....",
"....*.....*...**",
"*...****........",
"......***.*.*...",
"*.*...........**",
"...*..........**",
"....**.*......**",
".*****..........",
"...***...*...*.."]

for _ in range(C):
    clock_state_list = list(map(int,input().split()))

    def isAlign(clock_state_list):
        for clock_state in clock_state_list:
            if clock_state != 12:
                return False
        return True


    def push_switch(clock_state_list,switch_num):
        for clock_idx,char in enumerate(switches[switch_num]):
            if char == '*':
                clock_state_list[clock_idx] += 3
                if clock_state_list[clock_idx] == 15: clock_state_list[clock_idx] = 3
        return clock_state_list
    
    def solve(clock_state_list,switch_num):
        if switch_num == 10: #모든 스위치를 다 0~3번씩 눌렀을 때.
            if isAlign(clock_state_list):
                return 0
            else:
                return float('inf')
        
        ret = float('inf')
        for cnt in range(4):
            ret = min(ret,cnt + solve(clock_state_list,switch_num+1))
            clock_state_list = push_switch(clock_state_list,switch_num)
        return ret
    ret_v = solve(clock_state_list,0)
    if ret_v == float('inf'):
        ret_v = -1
    
    print(ret_v)
