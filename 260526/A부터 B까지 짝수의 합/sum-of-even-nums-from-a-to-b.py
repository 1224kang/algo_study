A,B=map(int,input().split())
sum=0

for x in range(A,B+1):
    if x%2==0:
        sum+=x

print(sum)