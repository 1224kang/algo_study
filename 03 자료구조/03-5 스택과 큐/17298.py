N=int(input()) #수열의 크기
arr=list(map(int,input().split())) #수열 입력받기
result=[0]*N
stack=[]

for i in range(N):
    while stack and arr[stack[-1]]<arr[i]: #스택이 비어있지 않고 현재수열값>스택 top 인덱스가 가리키는 수
        result[stack.pop()] = arr[i] #정답 리스트에 오큰수를 현재 수열로 저장
    stack.append(i) #append문의 위치 문제 😡

while stack: #반복문을 다 돌고 나왔는데 스택이 비어있지 않을 때 스택이 빌 때까지
    result[stack.pop()]=-1 # 스택에 쌓인 index에 -1 넣기

for i in range(N):
    print(result[i])