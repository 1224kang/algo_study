n=int(input()) #데이터의 개수
arr=list(map(int,input().split()))
sum=[0]*n

for i in range(1,n):
    insert_point=i
    insert_value=arr[i]
    for j in range(i-1,-1,-1):
        if arr[i]>arr[j]: #삽입 위치 결정
            insert_point=j+1
            break
        if j==0:
            insert_point=0


    for j in range(i,insert_point,-1):
        arr[j]=arr[j-1] #삽입 위치까지 한칸씩 미룸
    arr[insert_point]=insert_value #삽입


sum[0]=arr[0]
for i in range(n):
    sum[i]=sum[i-1]+arr[i]

s=0
for i in range(n):
    s+=sum[i]

print(s)

