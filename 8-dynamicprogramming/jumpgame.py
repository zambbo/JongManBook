def read_board(filepath):
    board = []
    for line in open(filepath,encoding='utf-8'):
        board.append(line.split())
    return board


def notValid(board,y,x,n):
    if y>=n or x>=n or y<0 or x<0: return True
    return False 

def jump_nodp(board,y,x):
    if notValid(board,y,x): return False
    if board[y][x] == -1: return True
    jump_size = int(board[y][x])

    return jump_nodp(board,y+jump_size,x) or jump_nodp(board,y,x+jump_size)

def init_memo(board):
    n = len(board[0])
    memo = [['x' for _ in range(n)] for _ in range(n)]
    return memo

def jump_dp(board,memo,y,x,n):
    if notValid(board,y,x,n): return False
    if board[y][x] == '-1': return True
    
    if memo[y][x] != 'x':
        return memo[y][x]
    jump_size = int(board[y][x])
    memo[y][x] = jump_dp(board,memo,y+jump_size,x,n) or jump_dp(board,memo,y,x+jump_size,n)
    return memo[y][x]


if __name__ == '__main__':
    board = read_board('./boardfile.txt')
    memo = init_memo(board)
    n = len(board[0])
    print(f"jump_dp :{jump_dp(board,memo,0,0,n)}")
