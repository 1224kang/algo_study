import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))
sum=[0]*n #[[0]*m]과 [0]*m 의 차이는 무엇인가.

print(sum)

sum[0]=arr[0]
remains=[0]*m
answer=0


#합 배열 구하기
for i in range(1,n):
    sum[i]=sum[i-1]+arr[i]

#나머지 배열 구하기
for i in range(n):
    remainders=sum[i]%m
    if remainders==0:
        answer+=1
    remains[remainders]+=1

#나머지 배열 원소 값이 같은 경우의 수 구하기
for i in range(m):
    if remains[i]>1:
        n=remains[i]
        answer+=(n*(n-1)//2)
print(answer)
