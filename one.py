#############################################
# 1. AVL TREE INSERT + INORDER TRAVERSAL
#############################################

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.height = 1

def height(n):
    return n.height if n else 0

def rotateRight(y):
    x = y.left
    y.left = x.right
    x.right = y
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    return x

def rotateLeft(x):
    y = x.right
    x.right = y.left
    y.left = x
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y

def balance(node):
    return height(node.left) - height(node.right)

def insert(root, key):
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    node = root
    node.height = 1 + max(height(node.left), height(node.right))
    b = balance(node)

    if b > 1 and key < node.left.key:
        return rotateRight(node)
    if b < -1 and key > node.right.key:
        return rotateLeft(node)
    if b > 1 and key > node.left.key:
        node.left = rotateLeft(node.left)
        return rotateRight(node)
    if b < -1 and key < node.right.key:
        node.right = rotateRight(node.right)
        return rotateLeft(node)
    return node

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

root = None
for x in [20, 10, 30, 5, 25]:
    root = insert(root, x)
print("1) AVL Inorder:", end=" ")
inorder(root)


###################################################
# 3. BI-CONNECTED COMPONENTS
###################################################

print("\n\n3) Bi-Connected Components:")

from collections import defaultdict
graph = defaultdict(list)
edges = [(0,1),(1,2),(2,0),(1,3),(3,4)]
for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)

def BCC():
    disc = [-1]*5
    low = [-1]*5
    stack = []
    time = 0

    def dfs(u, parent):
        nonlocal time
        disc[u] = low[u] = time
        time += 1

        for v in graph[u]:
            if disc[v] == -1:
                stack.append((u,v))
                dfs(v, u)
                low[u] = min(low[u], low[v])

                if low[v] >= disc[u]:
                    print("   BCC:", end=" ")
                    while stack[-1] != (u,v):
                        print(stack.pop(), end=" ")
                    print(stack.pop())
            elif v != parent:
                low[u] = min(low[u], disc[v])
                stack.append((u,v))

    dfs(0,-1)

BCC()


###################################################
# 5. DIJKSTRA SHORTEST PATH (GREEDY)
###################################################

print("\n5) Dijkstra Shortest Paths:")

import heapq
graph2 = {
    0: [(1,4),(2,1)],
    1: [(3,1)],
    2: [(1,2),(3,5)],
    3: []
}

def dijkstra(src):
    dist = {node: float("inf") for node in graph2}
    dist[src] = 0
    pq = [(0,src)]

    while pq:
        d, u = heapq.heappop(pq)
        for v, w in graph2[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(pq,(dist[v], v))
    return dist

print("   Distances from 0:", dijkstra(0))


###################################################
# 7. N-QUEENS
###################################################

def nqueen(n):
    col=set();d1=set();d2=set()
    board=[-1]*n
    ans=[]

    def bt(r):
        if r==n:
            for i in range(n):
                row=['.']*n
                row[board[i]]='Q'
                ans.append(''.join(row))
            return True
        for c in range(n):
            if c in col or r-c in d1 or r+c in d2: 
                continue
            board[r]=c
            col.add(c);d1.add(r-c);d2.add(r+c)
            if bt(r+1): return True
            col.remove(c);d1.remove(r-c);d2.remove(r+c)
        return False

    bt(0)
    return ans

n=4
sol=nqueen(n)
for row in sol: print(row)


###################################################
# 9. 0/1 KNAPSACK (DP)
###################################################

print("\n9) 0/1 Knapsack:")

def knap(W, wt, val, n):
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,W+1):
            if wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]

W = 7
wt = [1,3,4,5]
val = [1,4,5,7]
print("   Max Profit =", knap(W, wt, val, len(wt)))


###################################################
# 11. DIJKSTRA (MATRIX vs LIST)
###################################################

print("\n11) Dijkstra Using Matrix:")

mat = [
 [0,4,1,0],
 [4,0,2,1],
 [1,2,0,5],
 [0,1,5,0]
]

def dijkstra_matrix(src):
    n = len(mat)
    dist = [999]*n
    vis = [False]*n
    dist[src] = 0

    for _ in range(n):
        u = min((dist[i],i) for i in range(n) if not vis[i])[1]
        vis[u]=True
        for v in range(n):
            if mat[u][v] > 0:
                dist[v] = min(dist[v], dist[u] + mat[u][v])
    return dist

print("   Matrix Result:", dijkstra_matrix(0))


print("\n11) Dijkstra Using List:")

import heapq
graph3 = {
    0: [(1,4),(2,1)],
    1: [(3,1)],
    2: [(1,2),(3,5)],
    3: []
}

def dijkstra_list(src):
    dist = {i:999 for i in graph3}
    dist[src]=0
    pq=[(0,src)]
    while pq:
        d,u=heapq.heappop(pq)
        for v,w in graph3[u]:
            if d+w < dist[v]:
                dist[v]=d+w
                heapq.heappush(pq,(dist[v],v))
    return dist

print("   List Result:", dijkstra_list(0))



#############################################
# OUTPUT
#############################################

1) AVL Inorder: 5 10 20 25 30

3) Bi-Connected Components:
   BCC: (1, 3) (3, 4)
   BCC: (0, 1) (1, 2) (2, 0)

5) Dijkstra Shortest Paths:
   Distances from 0: {0: 0, 1: 3, 2: 1, 3: 4}

7)..Q.
Q...
...Q
.Q..


9) 0/1 Knapsack:
   Max Profit = 9

11) Dijkstra Using Matrix:
   Matrix Result: [0, 3, 1, 4]

11) Dijkstra Using List:
   List Result: {0: 0, 1: 3, 2: 1, 3: 4}
