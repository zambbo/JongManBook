adj = [[2],\
    [3],\
        [0,1],\
            [1]]

visited = [False]*len(adj)

def dfs(here):
    print(f"DFS visited: {here}")
    visited[here] = True

    for vertex in adj[here]:
        
        if not visited[vertex]:
            dfs(vertex)
        

def dfsAll():
    for vertex in range(len(adj)):

        if not visited[vertex]:
            dfs(vertex) 

if __name__ == '__main__':
    dfsAll()