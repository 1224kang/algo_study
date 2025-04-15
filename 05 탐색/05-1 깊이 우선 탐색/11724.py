import sys
sys.setrecursionlimit(1000) #재귀 호출의 최대 깊이를 1000으로 설정
input=sys.stdin.readline
n,m=map(int,input().split())
A=[[] for _ in range(n+1)] #인접 리스트 초기화
visited=[False]*(n+1) #방문 리스트 초기화

#DFS 정의
def DFS(v):
    visited[v]=True #현재 노드 True
    for i in A[v]:
        if not visited[i]: #현재 노드의 연결 노드 중 방문하지 않은 노드로 DFS 실행
            DFS(i)

#인접 그래프 -> 인접 리스트
for i in range(m):
    s,e=map(int,input().split())
    A[s].append(e)
    A[e].append(s)

count=0

#노드를 돌면서 DFS 수행
for i in range(1,n+1):
    if not visited[i]:
        count+=1
        DFS(i)

print(count)