n, m = map(int, input().split())

# Please write your code here.
def gcd(n,m):
    num=min(n,m)
    answer=1
    for x in range(1,num+1):
        if n%x==0 and m%x==0:
            answer=x
    print(answer)

gcd(n,m)