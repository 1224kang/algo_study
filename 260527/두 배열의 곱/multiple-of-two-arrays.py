arr1=[list(map(int,input().split())) for _ in range(3)]
input()
arr2=[list(map(int,input().split())) for _ in range(3)]

for i in range(3):
    new_arr=[]
    for j in range(3):
        new_arr.append(arr1[i][j]*arr2[i][j])
    print(*new_arr)