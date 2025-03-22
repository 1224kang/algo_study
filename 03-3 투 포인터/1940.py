import sys
input=sys.stdin.readline

n=int(input()) #재료의 개수
m=int(input()) #갑옷이 완성되는 번호의 합
arr=list(map(int,input().split()))
arr.sort() #오름차순 정렬

count=0
i=0
j=n-1


#리스트의 양 끝에 두 개의 포인터를 각각 위치 -> 두 포인터가 만나게 되면 종료⭐
while i<j:
    if arr[i]+arr[j]==m:
        i+=1
        j-=1
        count+=1
    elif arr[i]+arr[j]>m:
        j-=1
    else:
        i+=1

print(count)

