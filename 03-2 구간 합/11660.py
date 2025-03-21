import sys
input=sys.stdin.readline

n,m=map(int,input().split()) #2차원 배열의 크기, 구간 합 질의 개수
arr=[[0]*(n+1)]
sum=[[0]*(n+1) for _ in range(n+1)]
temp=0

#정답 참고
for i in range(n):
    row=[0]+[int(x) for x in input().split()] #생성된 문자열 리스트를 정수 리스트로 변환
    arr.append(row)

#합 배열 만들기
for i in range(1,n+1):
    for j in range(1,n+1):
        sum[i][j]=sum[i][j-1]+sum[i-1][j]+sum[i-1][j-1]+arr[i][j]

#구간 합 질의 응답
for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    ans=sum[x2][y2]-sum[x1-1][y2]-sum[x2][y1-1]+sum[x1-1][y1-1]
    print(ans)