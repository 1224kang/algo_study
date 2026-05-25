N=int(input())
arr=list(map(int,input().split()))
list=[]

for i in arr:
    if i%2==0:
        list.append(i)

list.reverse()
print(*list)