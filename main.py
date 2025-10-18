import sys
import heapq
input = sys.stdin.readline

n,m,x = map(int,input().split())
G = [[] for i in range(n+1)]

for i in range(m):
    s,e,t = map(int,input().split())
    G[s].append((e,t))

def distance(x):
    global n
    queue = []
    dist = [float('inf') for i in range(n + 1)]
    heapq.heappush(queue,(0,x))
    dist[x]=0
    while queue:
        w,cn = heapq.heappop(queue)
        for nn,nw in G[cn]:
            if nw+dist[cn] < dist[nn]:
                dist[nn] = nw+dist[cn]
                heapq.heappush(queue,(dist[nn],nn))
    return dist
ans = 0
d = distance(x)
for i in range(1,n+1):
    if i == x:
        continue
    p = distance(i)
    if d[i]+p[x] > ans:
        ans = d[i]+p[x]
print(ans)
# 백준 파티 문제
