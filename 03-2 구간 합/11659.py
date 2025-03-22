import sys
input=sys.stdin.readline

n,m=map(int,input().split())
sum=[0]
num=list(map(int,input().split()))
temp=0

#합 배열 구하기
for i in num:
    temp=temp+i
    sum.append(temp)

print(sum)

#구간 합 구하기
for i in range(m):
    start,end=map(int,input().split())
    print(sum[end]-sum[start-1])