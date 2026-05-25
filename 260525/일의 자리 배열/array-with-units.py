arr=list(map(int,input().split()))

for i in range(8):
    next_val=(arr[-1]+arr[-2])%10
    arr.append(next_val)

print(*arr)