N=int(input())
arr=[x for x in range(1,N+1)]
new_arr=[]

for i in range(1,N+1):
        if(i%2==0):
            print(*arr[::-1],sep="")
        else:
            print(*arr,sep='')