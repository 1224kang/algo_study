N=int(input())

for _ in range(N):
    sum=0
    a,b=map(int,input().split())
    for j in range(a,b+1):
        if j%2==0:
            sum+=j
    print(sum)
