from queue import PriorityQueue

N=int(input()) #연산의 개수
myQueue=PriorityQueue()

for i in range(N):
    request=int(input())
    if request==0:
        if myQueue.empty():
            print("0")
        else:
            temp=myQueue.get()
            print(temp[1])
    else:
         # 1.절댓값 기준 정렬(abs(request)),2. 음수 우선 정렬(request)
         # ⭐ 우선순위 큐 정렬 기준을 새로 만들기
        myQueue.put((abs(request),request))