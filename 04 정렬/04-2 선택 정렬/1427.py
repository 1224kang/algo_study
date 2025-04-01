#선택 정렬
N=list(input())

for i in range(len(N)):
    Max=i
    for j in range(i+1,len(N)):
        if N[j]>N[Max]:
            Max=j
    if N[i]<N[Max]:
        temp=N[i]
        N[i]=N[Max]
        N[Max]=temp

for i in N:
    print(i)


#버블 정렬
N=list(input())

for i in range(len(N)-1):
    for j in range(len(N)-1-i):
        if N[j]>N[j+1]:
            temp=N[j]
            N[j]=N[j+1]
            N[j+1]=temp
        