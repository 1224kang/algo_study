n = int(input())

# Please write your code here.
def make_square(n):
    num=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(num,end=" ")
            num+=1
            if num==10:
                num=1
        print()

make_square(n)