


C = int(input())

for _ in range(C):
    N = int(input())

    preorder = list(map(int,input().split()))
    inorder = list(map(int,input().split()))

    def printPostorder(preorder, inorder):
        n = len(preorder)

        if n == 0: return

        root = preorder[0]

        L = inorder.index(root)# 왼쪽 트리의 노드 개수
        R = n - L - 1 # 오른쪽 트리의 노드 개수

        printPostorder(preorder[1:L+1], inorder[0:L])
        printPostorder(preorder[L+1:], inorder[L+1:])
        print(root, end=' ')
    printPostorder(preorder, inorder)