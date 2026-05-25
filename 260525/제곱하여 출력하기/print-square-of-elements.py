

N=int(input())
a=list(map(int,input().split()))
answer=[x**2 for x in a]

print(*answer)