import sys
input=sys.stdin.readline

N=int(input())
arr=[]

for i in range(N):
    arr.append((int(input()),i)) #(데이터 값, 인덱스)

sorted_arr=sorted(arr)
Max=0

for i in range(N):
    #정렬 전 index-정렬 후 index
    if Max<sorted_arr[i][1]-i:
        Max=sorted_arr[i][1]-i

print(Max)

