N=5

board = []
board.append(['N','N','N','N','S'])
board.append(['N','E','E','E','N'])
board.append(['N','E','Y','E','N'])
board.append(['N','E','E','E','N'])
board.append(['N','N','N','N','N'])

def outOfIndex(y, x, N):
    if y>=N or x>=N or y<0 or x<0:
        return True
    return False

dx_list = [-1,-1,-1,0,0,1,1,1]
dy_list = [-1,0,1,1,-1,-1,0,1]

def hasWord(y, x, word):
    if outOfIndex(y, x, N):
        return False
    if board[y][x] != word[0]:
        return False
    if len(word) == 1:
        return True
    
    for dx, dy in zip(dx_list,dy_list):
        next_x = x+dx
        next_y = y+dy
        if hasWord(next_y,next_x,word[1:]):
            return True
    
    return False
print(board[2][2])
print(hasWord(2,2,"YEK"))
print(hasWord(2,2,"YES"))