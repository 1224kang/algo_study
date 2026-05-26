N=int(input())
sum=0

for x in range(1,101):
    sum+=x
    if sum>=N:
        break

print(x)