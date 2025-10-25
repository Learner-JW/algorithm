# import heapq
# import sys
# input = sys.stdin.readline
#
# N=int(input())
# M=int(input())
# # 인접 행렬
# G=[[100000 for i in range(N+1)]for i in range(N+1)]
# for i in range(M):
#     node1,node2,weight=map(int,input().split())
#     G[node1][node2]=weight
# for i in range(1,N+1):
#     G[i][i]=0
#
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         print(G[i][j],end=' ')
#     print()
# print()
# # 플로이드 와셜 (i = 거쳐가는 노드 , j=시작노드, k = 도착노드)
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         for k in range(1,N+1):
#             #if i==j or i==k or j==k:continue
#             if G[j][k]>G[j][i]+G[i][k]:
#                 G[j][k]=G[j][i]+G[i][k]
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         print(G[i][j],end=' ')
#     print()


# A=[4,2,3,0,1]

# S=   [0,0,1,0,1]
# L=   [0,1,0,1,0]
# idx= [0,1,2,3,4]
#
# idx-s[idx]= 왼쪽에 나보다 큰 친구의 수
# L[idx] = 오른쪽에 나보다 큰 친구의 수
#
# print(N-(idx-s[idx])-L[idx]-1)


S=list(map(int,input().split()))
L=list(map(int,input().split()))
A=[0]*len(S)
N=len(S)-1
for i in range(len(S)):
    A[i]=N-(i-S[i])-L[i]
print(A)
