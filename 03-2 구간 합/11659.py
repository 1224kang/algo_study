n,m=map(int,input().split()) #데이터의 개수, 질의 개수
arr=list(map(int,input().split()))
sum=[0]
temp=0


#구간 합을 구할 대상 배열 입력 받기
for i in arr:
    temp=temp+i #arr 배열 안에서 for문 i는 arr[i]로 표현하지 않아도 i는 자연스럽게 arr[i] 값을 가리킴
    sum.append(temp) #합 배열 구하기

print(sum)

# 구간 합 구하기
for i in range(m):
    start,end=map(int,input().split())
    print(sum[end]-sum[start-1])

