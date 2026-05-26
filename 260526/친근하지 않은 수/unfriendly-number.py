N=int(input())

count=0
for x in range(1,N+1):
    if x%2==0:
        continue
    elif x%3==0:
        continue
    elif x%5==0:
        continue
    else:
        count+=1

print(count)