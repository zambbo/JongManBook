C = int(input())

coverType = [[(0,0),(1,0),(0,1)],[(0,0),(0,1),(1,1)],[(0,0),(1,0),(1,1)],[(0,0),(1,0),(1,-1)]]


for _ in range(C):
    H, W = map(int,input().split())

    board = [['.']*W for _ in range(H)]

    for i in range(H):
        line = input()
        for j,char in enumerate(line):
            if char == '#':
                board[i][j] = char

    def cover(board):
        y, x = -1, -1

        for i in range(H):
            for j in range(W):
                if board[i][j] == '.':
                    y = i
                    x = j
                    break
            if y !=-1: break
        
        if y == -1:
            return 1

        ret = 0
        def isValidCover(board,cover_type):
            for dy, dx in cover_type:
                new_y, new_x = y+dy, x+dx
                if new_y < 0 or new_x < 0 or new_y >= H or new_x >= W or board[new_y][new_x] == '#':
                    return False
            return True 

        for cover_type in coverType:
            if isValidCover(board, cover_type):
                for dy,dx in cover_type:
                    new_y, new_x = y+dy, x+dx
                    board[new_y][new_x] = '#'
                ret += cover(board)
                for dy, dx in cover_type:
                    new_y, new_x = y+dy, x+dx
                    board[new_y][new_x] = '.'
        return ret

    print(cover(board))