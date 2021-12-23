
def read_triangle(file_path):
    triangle = []
    for line in open(file_path,encoding="utf-8"):
        triangle.append(line.split())
    return triangle


triangle = read_triangle('./triangle.txt')


memo = [[['x' for _ in range(1000)] for _ in range(100)] for _ in range(100)]

def pathSum(y, x, sum):
    
    if y == len(triangle) -1:
        return sum + int(triangle[y][x])
    

    if memo[y][x][sum] != 'x':
        return memo[y][x][sum]
    init_sum = sum
    sum += int(triangle[y][x])
    memo[y][x][init_sum] = max(pathSum(y+1,x,sum),pathSum(y+1,x+1,sum))
    print(y,x,sum)

    return memo[y][x][init_sum]

print(pathSum(0,0,0))