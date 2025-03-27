N=int(input()) #수열의 개수
A=[0]*N
stack=[] #스택
result=[]
num=1

#수열 입력받기
for i in range(N):
    A[i]=int(input())

for i in range(N):
    while num<=A[i]:
        stack.append(num)
        num+=1
        result.append('+')
    if stack[-1]==A[i]:
        stack.pop()
        result.append('-')
    else:
        result=False
        break

if result:
    for i in result:
        print(i)
else:
    print("NO")