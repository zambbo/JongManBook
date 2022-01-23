

def partialSum(_originalList):
    ps_list = []
    sum = 0
    for value in _originalList:
        sum += value
        ps_list.append(sum)
    
    return ps_list

def rangeSum(_ps_List, a, b):
    low = _ps_List[a-1] if a >= 1 else 0
    high = _ps_List[b]
    return high-low

def sqpartialSum(_originalList):
    sqps_list = []
    sq_sum = 0
    for value in _originalList:
        sq_sum += value**2
        sqps_list.append(sq_sum)
    return sqps_list 

def variance(_sqps_list, _ps_list, a, b):
    length = b-a+1
    mean = rangeSum(_ps_list,a,b) / length
    
    f = rangeSum(_sqps_list,a,b)
    m = -2*mean*rangeSum(_ps_list,a,b)
    l = length * mean**2
    return (f+m+l)/length


list = list(map(int,input().split()))
sqps_list = sqpartialSum(list)
ps_list = partialSum(list)
print(variance(sqps_list,ps_list,0,4))