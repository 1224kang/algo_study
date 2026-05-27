arr=[list(map(int,input().split())) for _ in range(3)]
result=[[num*3 for num in row] for row in arr]

for row in result:
    print(*row)
