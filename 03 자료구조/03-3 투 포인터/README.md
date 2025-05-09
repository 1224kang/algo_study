## 투포인터
> **포인터** = 프로그래밍 언어에서 다른 변수, 혹은 그 변수의 메모리 공간 주소를 가리키는 변수
- 리스트에 순차적으로 접근해야 할 때 **두 개의 점 위치를 기록하면서 처리** 하는 알고리즘
- 보통 ```O(n)``` 의 시간 복잡도를 가짐 

⭐ **파이썬에서의 포인터** : 파이썬에서는 별도의 포인터가 존재 X. 대신, ```id함수```가 존재하는데, 이는 객체가 메모리에서 어디에 위치해 있는지 알려주는 함수이다. 
쉽게 말하면, **객체의 메모리주소를 반환** 해준다고 생각하면 된다.

<br/>

⭐ 파이썬에서의 **가변 객체 vs. 불변 객체**
- **불변 객체**에서 값이 바뀌었을 때는 값이 바뀐 것✖️, **메모리주소**가 바뀐 것이다. 
<br/>불변 객체에서는 메모리 내의 데이터를 바꿀 수 없으므로, 
1. 같은 객체 할당 시, 최적화를 위해 같은 메모리 주소를 할당하거나 
2. 다른 객체로 바뀌면 다른 메모리 주소에 새로운 값을 넣고 변수가 가리키는 주소를 새로운 메모리 주소로 바꿔주는 방식을 사용한다.
<br/>
- 반면 **가변 객체**에서 값이 바뀌면, **메모리 주소가 바뀌지✖️**, 불변 객체에 비해 데이터의 추가, 수정, 삭제가 자유롭다. 
그래서 보통 값이 바뀌어도 **기존 메모리 주소를 할당**한다.
<br/>
∴ 파이썬은 자체적으로 포인터를 활용하지만, 할당하려는 객체가 **가변인지, 불변인지**에 대해 다르게 작동된다.

---

### 2018 : 연속된 자연수의 합 구하기
✏️ 투 포인터 이동 원칙 
```commandline
- sum>N: sum=sum-start_index; start_index++;
- sum<N: end_index++; sum=sum+end_index;
- sum==N: end_index++; sum=sum+end_index; count++;
```
---
### 1253 : '좋은 수' 구하기
✏️
1. 리스트를 오름차순 배열
2. start_index와 end_index를 리스트 양쪽에 위치
3. 큰 수부터 좋은 수인지 확인(```j``) 하기 위해 역반복문 사용
   (이 때, end_index는 j보다 인덱스가 무조건 한 칸 앞에 있는 것부터 시작해야 함  )
4. ```start_index<end_index``` 를 while 반복문 조건으로 사용하여 이 조건 내에서 ```arr[j]==start_index+end_index```를 만족하는 것이 없다면 해당 j는 좋은 수가 아닌 것
5. 만약 ```arr[j]==start_index+end_index``` 를 만족하면, break문을 통해 바로 다음 숫자가 좋은 수인지 알아보기


✏️ 좋은 수가 될수 있는 모든 경우의 수를 구하는 것이 아닌, 좋은 수의 개수를 구하는 것 ‼️
<br/> while문과 ```break```를 적절히 잘 사용할 수 있어야 함
