import sys
input=sys.stdin.readline

n,m=map(int,input().split()) #배열 원소 개수,배열 원소들
arr=list(map(int,input().split())) #내가 만든 배열
sum=[0]*n #합 배열
indexes=[0]*m#같은 원소값의 인덱스 저장
answer=0 #

sum[0]=arr[0]

#합 배열 구하기
for i in range(1,n):
    sum[i]=arr[i]+sum[i-1]

#나머지 합 배열 구하기
for j in range(n):
    remain=sum[j]%m
    if remain==0: #나머지가 0인 경우 정답에 추가
        answer+=1
    indexes[remain]+=1 #나머지가 0이 아닌 경우 인덱스 추가

#같은 인덱스 저장q
for i in range(m):
    if (indexes[i]>1):
        n=indexes[i]
        answer+=(n*(n-1))//2 # / -> float 형태로 소수점까지 출력해 오류 발생.


print(answer)

### remain 관련 배열을 만들 필요가 없었음. 합배열 -> 나머지 배열로 변환하면 배열 개수를 줄이면서 충분히 연산 가능
### for문으로 반복문을 돌 때, range(m)일 때와 배열 자체 중 어떤 걸로 해야 할지 고민 필수