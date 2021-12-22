C = int(input())

for _ in range(C):
    fence_num = int(input())
    fence_list = list(map(int,input().split()))

    def getMaxFenceArea(left, right):
        
        if left==right:
            return fence_list[left]
        
        mid = (left + right) // 2

        ret = max(getMaxFenceArea(left,mid),getMaxFenceArea(mid+1,right))

        lo = mid
        hi = mid+1

        height = min(fence_list[lo],fence_list[hi])

        ret = max(ret,2*height)

        while left < lo or hi < right:

            if hi < right and (left == lo or fence_list[lo-1] < fence_list[hi+1]):
                hi += 1
                height = min(height,fence_list[hi])
            else:
                lo -= 1
                height = min(height,fence_list[lo])
            
            ret = max(ret,(hi-lo+1) * height)
        
        return ret

    print(getMaxFenceArea(0,fence_num-1))

