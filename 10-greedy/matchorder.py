rus_list = [3000,2700,2800,2200,2500,1900]
kor_list = [2800,2750,2995,1800,2600,2000]

def order(rus_list, kor_list):
    match_list = []
    wins = 0
    kor_list = sorted(kor_list, reverse=False)
    for rus in rus_list:
        # 만약 한국 팀중 가장 레이팅이 높은 사람이 러시아 팀 보다 낮을 경우
        if rus > kor_list[-1]:
            match_list.append(kor_list[0])
            del kor_list[0]
        # 이길 수 있는 한국 팀중 가장 낮은 선수와 매칭
        else:
            for idx in range(len(kor_list)-1,-1,-1):
                if rus > kor_list[idx]:
                    match_list.append(kor_list[idx+1])
                    del kor_list[idx+1]
                    break
            
            wins += 1
    return wins,match_list



if __name__ == '__main__':
    print(order(rus_list,kor_list))