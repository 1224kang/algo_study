

myList=[0]*4 # 내 비밀번호 리스트
secretCheck=0 #유효한 비밀번호 문자 조건을 만족하는 개수
result=0
checkList=[0]*4



# 슬라이딩 윈도우 오른쪽 이동 -> 문자 추가
def myadd(c):
    global secretCheck,checkList,myList
    if c=='A':
        myList[0]+=1
        if myList[0]==checkList[0]:
            secretCheck+=1

    elif c=='C':
        myList[1]+=1
        if myList[1]==checkList[1]:
            secretCheck+=1

    elif c=='G':
        myList[2]+=1
        if myList[2]==checkList[2]:
            secretCheck+=1

    elif c=='T':
        myList[3]+=1
        if myList[3]==checkList[3]:
            secretCheck+=1


# 슬라이딩 윈도우 오른쪽 이동 -> 문자 삭제
def myremove(c):
    global secretCheck,checkList,myList
    if c=='A':
        myList[0]-=1
        if myList[0]==checkList[0]:
            secretCheck-=1
    elif c=='C':
        myList[1]-=1
        if myList[1]==checkList[1]:
            secretCheck-=1
    elif c=='G':
        myList[2]-=1
        if myList[2]==checkList[2]:
            secretCheck-=1
    elif c=='T':
        myList[3]-=1
        if myList[3]==checkList[3]:
            secretCheck-=1

n,m=map(int,input().split()) #DNA 문자열의 길이, 부분 문자열의 길이
dna=list(input()) #DNA 문자열
checkList=list(map(int,input().split())) #부분 문자열에 포함되어야 할 A,C,G,T의 최소 개수


# 유효 조건이 특정문자가 0개 이상인 경우는 바로 유효하다고  검사.
for i in range(4):
    if checkList[i]==0:
        secretCheck+=1


#초기  myList 검사
for i in range(m):
    myadd(dna[i])
    if secretCheck==4:
        result+=1


# 한 칸씩 이동하면서 유효한 비밀번호인지 체크
for i in range(m,n):
    j=i-m
    myremove(dna[j])
    myadd(dna[i])
    if secretCheck==4:
        result+=1

print(result)

