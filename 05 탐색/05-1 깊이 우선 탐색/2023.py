import sys,math
sys.setrecursionlimit(10000)
input=sys.stdin.readline

N=int(input())


## 개별 소수 판별
# def isPrime(num):
#     for i in range(2,int(num/2+1)):
#         if num%i==0:
#             return False
#     return True


def isPrime(n):

    global is_prime
    is_prime=[True]*(n+1)
    is_prime[1]=False

    for i in range(2,int(math.sqrt(n))+1):
        if is_prime[i]: #i가 소수일 때
            for j in range(i*2,n+1,i):#i의 배수들은 소수일 수 없다
                is_prime[j]=False
    return is_prime


## 개별 소수 판별
# def DFS(number):
#     if len(str(number))==N:
#         print(number)
#     else:
#         for i in range(1,10): #i가 현재
#             if i%2==0:
#                 continue
#             if isPrime(number*10+i):
#                 DFS(number*10+i)


def DFS(number):
    if len(str(number))==N:
        print(number)
    else:
        for i in range(1,10):
            if is_prime[number*10+i]:
                DFS(number*10+i)
#일의 자리 소수는 2,3,5,7이므로 4가지 수에서만 시작

isPrime(10**N) #isPrime(10*n)이라 했었음.. -> number*10+i가 10*N보다 커지는 문제 발생 ⚠️
DFS(2)
DFS(3)
DFS(5)
DFS(7)