import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
arrive=False
N,M=map(int,input().split())
A=[[] for _ in range(N+1)]
visited=[False]*(N+1)



def DFS(num,depth):
    global arrive

    if depth==5: #깊이가 5가 되면 종료
        arrive=True
        return

    visited[num]=True
    for i in A[num]:
        if not visited[i]:
            DFS(i,depth+1) #매번 depth를 함수 인자로 넘기고, 한 단계식 올려가야 정확히 깊이 5를 검사할 수 있음

    visited[num]=False #백트래킹을 위해. 방문한 후 되돌아갈 때 방문표시를 다시 해야 다른 경로에서 이 노드를 사용 가능.


for _ in range(M):
    s,e=map(int,input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(N):
    DFS(i,1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)