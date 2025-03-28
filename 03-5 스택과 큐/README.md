## 03-5. 스택과 큐

### 스택(Stack) 
➡️ 후입선출(LIFO)
- ```리스트``` 활용하여 구현 

✏️ 위치
- ```top``` : 삽입&삭제가 일어나는 위치

✏️연산
- ```s.append(data)``` : top 위치에 새로운 데이터를 삽입
- ```s.pop()```: top 위치에 현재 있는 데이터를 삭제하고 확인하는 연산
- ```s[-1]``` : top 위치에 현재 있는 데이터를 단순 확인하는 연산 

✏️ex
- 브라우저의 뒤로가기
- 실행 취소(Ctrl+z)
- 재귀 함수
- 역순 문자열(문자열 거꾸로 뒤집기)

✏️시간 복잡도
- 삽입, 삭제 : ```O(1)```
- 탐색 : ```O(n)```
<br/><br/>

### 큐(Queue)
➡️ 선입선출(FIFO)

✏️ 위치
- ```rear``` : 큐에서 ```가장 끝 데이터```를 가리키는 영역
- ```front``` : 큐에서 ```가장 앞 데이터```를 가리키는 영역 

✏️ 연산
- ```s.append(data)```:rear 부분에서 새로운 데이터 삽입
- ```s.popleft()```:front 부분 데이터 삭제,확인
- ```s[0]```: 큐의 맨 앞(front)에 있는 데이터를 확인할 때 사용 

✏️ ex
- BFS 알고리즘
- 프린터 대기열 

✏️시간 복잡도
- 삽입, 삭제 : ```O(1)```
- 탐색 : ```O(n)```
---
### 1874 : 스택으로 수열 만들기
✏️ 수열이 주어지면 스택을 이용해서 해당 수열을 만들어야
이떄, 주의해야 할 점 !! push연산, pop연산 외에 수열을 만들 수 없는 불가능한 경우가 언제인지를 생각해야 함. 

😡 나는 직접 올림차순 배열을 따로 만들어서 여기서 인덱스를 하나씩 늘어나도록 하여 주어진 수열의 값과 비교하는 방식을 사용하려고 시도함.
하지만 책에서는 별도의 오름차순 배열을 만들지 않고 num=1로 숫자로 설정하여 이를 하나씩 늘여가면서 수열의 값과 비교하는 방식 채택. 
하지만 이 경우에는 만약 입력된 수열의 크기가 8인데, 1~8이 입력되지 않고 1,2,3,4,6,7,8,9 이런 식으로 입력되면 달라지지 않나? 

바보야!! num 숫자 자체와 비교하는게 아니고 num을 하나씩 크게 해서 기존 수열과 비교해 조건에 만족하는 애들만 stack에 저장하는 거였잖슴~
∴ num과 stack 중 비교를 어떻게 하는지와 for, while문을 적절히 사용해야 하는 부분을 주의해야 함
---
### 17298 : 오큰 수 구하기
✏️ **스택 활용**
인덱스를 활용해야 하는 것이 가장 큰 중요한 점이다. 
```pop``` : 해당 인덱스의 오큰수가 stack의 top을 만족할 때
```append``` : 수열의 다음 인덱스를 보려고 할 때 (만약 해당 인덱스의 오큰수가 없다면 해당 인덱스는 스택에 계속 남아있게 됨 -> 마지막까지 스택에 남아있는 인덱스들은 오큰수가 존재하지 않고 -1이 됨)

⭐ 스택에 인덱스로 저장하니 오큰수 배열에 어떤 걸 저장해야 할지 헷갈렸다. 이렇게 생각하면 간단하다!
pop 당시 stack[top] 인덱스가 가지는 값이 바로 오큰수이다.