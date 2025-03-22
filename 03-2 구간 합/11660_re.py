import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[[0]*(n+1)] #(n+1)인 것 주의
sum=[[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    num=[0]+list(map(int,input().split()))
    num.append(arr)

print(arr)

#합 배열 구하기
for i in range(1,n+1):
    for j in range(1,n+1):
        sum[i][j]=sum[i-1][j]+sum[i][j-1]-sum[i-1][j-1]+arr[i][j]

#구간합 배열 구하기
for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    result=sum[x2][y2]-sum[x1-1][y2]-sum[x2][y1-1]+sum[x1-1][y1-1] #구간 합 배열 구하는 부분 로직 검토 필수
    print(result)