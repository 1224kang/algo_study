import sys


input=sys.stdin.readline

N,K=map(int,input().split())
A=list(map(int,input().split()))

#swap 함수
def swap(i,j):
    temp=A[i]
    A[i]=A[j]
    A[j]=temp

#partition 함수 - pivot 정하기⭐
def partition(S,E):
    global A

    #리스트 내에 숫자가 2개 밖에 없는 경우
    if S+1==E:
        if A[S]>A[E]:
            swap(S,E)
        return E

    #리스트의 가운데에 있는 것을 pivot으로 설정
    M=(S+E)//2
    swap(S,M) #중앙값을 시작 위치와 swap(∵ i,j 이동을 편하게 하기 위함)
    pivot=A[S]
    i=S+1
    j=E

    while i<=j:
        while pivot<A[j] and j>0:
            j-=1
        while pivot>A[i] and i>len(A)-1:
            i+=1
        if i<=j:
            swap(i,j)
            i+=1
            j-=1

    A[S]=A[j]
    A[j]=pivot
    return j

#퀵 정렬 함수
def quickSort(S,E,K):
    global A
    if S<E:
        pivot=partition(S,E)
        if pivot==K: #K번째 수가 pivot이면 더는 구할 수 없ㅇ슴
            return # 현재 함수 종료 ⭐
        elif K<pivot: #K가 pivot보다 작으면
            quickSort(S,pivot-1,K)
        else:
            quickSort(pivot+1,E,K)

quickSort(0,N-1,K-1)
print(A[K-1])