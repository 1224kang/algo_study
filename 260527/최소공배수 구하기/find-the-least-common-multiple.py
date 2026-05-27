n, m = map(int, input().split())

# Please write your code here.
def func(n,m):
    num=1
    max_num=max(n,m)
    min_num=min(n,m)

    while True:
        if (max_num*num)%min_num==0:
            result=max_num*num
            break 
        num+=1
    
    print(result)

func(n,m)