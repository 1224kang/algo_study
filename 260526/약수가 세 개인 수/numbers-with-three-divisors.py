start, end = map(int, input().split())
count=0
cnt=0

# Please write your code here.
for x in range(start,end+1):
    count=0
    for j in range(1,x+1):
        if x%j==0:
            count+=1
    if count==3:
        cnt+=1

print(cnt)