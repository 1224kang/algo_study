import sys
from turtledemo.penrose import start

input=sys.stdin.readline

n=int(input()) #수의 개수
arr=list(map(int,input().split()))
arr.sort() #오름차순 정렬
count=0

#양 쪽의 투 포인터로 시작
for k in range(n,0,-1):
    start_index=0
    end_index=k-1
    while start_index<end_index:
        if k==arr[start_index]+arr[end_index]:
            count+=1
            break
        elif k>arr[start_index]+arr[end_index]:
            start_index+=1
        else:
            end_index-=1

print(count)