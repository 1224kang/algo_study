N=int(input())
list=[]

for score in range(101-N):
    if(N>=90):
        list.append("A")
    elif(N>=80):
        list.append("B")
    elif(N>=70):
        list.append("C")
    elif(N>=60):
        list.append("D")
    else:
        list.append("F")
    N+=1

print(' '.join(list))