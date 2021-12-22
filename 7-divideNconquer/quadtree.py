C = int(input())

for _ in range(C):
    compressed_quadtree = str(input())


    def ReverseQuadTree(quadtree):
        if quadtree[0] == 'w' or quadtree[0] == 'b':
            return quadtree[0],1


        topleft, offset1 = ReverseQuadTree(quadtree[1:])
        topright, offset2 = ReverseQuadTree(quadtree[1+offset1:])
        bottomleft, offset3 = ReverseQuadTree(quadtree[1+offset1+offset2:])
        bottomright, offset4 = ReverseQuadTree(quadtree[1+offset1+offset2+offset3:])


        return 'x'+bottomleft+bottomright+topleft+topright, offset1+offset2+offset3+offset4+1 # 1을 더하는 이유는 현재 return 은 'x'가 있을 경우의 return이기때문에 'x' 자리수만큼 또 더해줘야 함이다.
    print(ReverseQuadTree(compressed_quadtree)[0])
                 

