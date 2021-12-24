C = int(input())

for _ in range(C):
    n = int(input())

    sn_list = list(map(int,input().split()))

    def concat(sn_list):
        sn_list = sorted(sn_list, reverse = False)
        ret = 0
        while len(sn_list) > 1:
            ret += (sn_list[0] + sn_list[1])
            insert_item = sn_list[0] + sn_list[1]
            del sn_list[0]
            del sn_list[0]

            for i in range(len(sn_list)):
                if sn_list[i] >= insert_item:
                    sn_list.insert(i,insert_item)
                    break
                if i == len(sn_list)-1:
                    sn_list.append(insert_item)
        return ret
            
        

    print(concat(sn_list))