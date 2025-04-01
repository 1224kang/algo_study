N=int(input()) #수의 개수
arr=[0]*N

for i in range(N):
    num=int(input())
    arr[i]=num

for i in range(N-1):
    for j in range(N-1-i): #이미 정렬된 상태인 것들 제외
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp

for i in arr:
    print(i)