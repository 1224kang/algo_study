line=[list(map(int,input().split())) for _ in range(4)]

for i in range(4):
    sum=0
    for num in line[i]:
        sum+=num
    print(sum)