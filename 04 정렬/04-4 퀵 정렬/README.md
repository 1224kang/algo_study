## 퀵 정렬
> 기준값(pivot)을 선정해 해당 값보다 작은 데이터와 큰 데이터로 분류하는 것을 반복해 정렬하는 알고리즘
<br/>
- 평균적인 시간 복잡도 : ```O(nlogn)```
- 최악의 경우 : ```O(n^2)```
<br/>**⭐ ```pivot```이 어떻게 설정되느냐가 중요**
<br/>⭐  **재귀함수** 형태로 구현 
<br/>

**퀵 정렬 과정**
```
1. pivot 설정
2. pivot 기준으로 데이터를 2개의 집합으로 분리
2-1. start<pivot : start++
2-2. end>pivot : end--
2-3. start>pivot && end<pivot:
   start&end **swap**;
   start++;
    end--;
2-4. start==end:
   if start>pivot:
    pivot=start+1
   else:
    pivot=start-1
3. 분리 집합에서 다시 각각 pivot 설정
4. 분리 집합이 1개 이하가 될 때까지 과정 반복 
```
---
### 11004 : K번째 수 구하기
✏️ 퀵 정렬 함수, 피벗 구하기 함수를 별도로 정의 
1. 중간 위치를 pivot으로 설정 -> 맨 앞에 있는 값과 swap (∵ i,j 이동을 편하게 하기 위함)
2. 이어서 i와 j를 pivot을 제외한 그룹에서 왼쪽, 오른쪽 끝으로 정함
3. i==j가 되면, pivot을 두 집합을 나눠주는 위치(=i와 j가 만난 위치) 와 swap 
<br/>
<br/><br/>
**pivot을 정하는 방법**
```
- pivot==K : K번째 수를 찾은 것이므로 알고리즘 종료
- pivot>K : pivot의 왼쪽 부분에 K가 있으므로 왼쪽(S~pivot-1)만 정렬을 수행
- pivot<K : pivot의 오른쪽 부분에 K가 있으므로 오른쪽(pivot+1~E) 만 정렬 수행 
```