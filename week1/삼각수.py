# 삼각수를 구하는 함수
def triangular_number(n):
    return n * (n + 1) // 2


# 주어진 숫자를 3개의 삼각수의 합으로 표현할 수 있는지 확인하는 함수
def is_eureka_number(number):
    # 삼각수를 리스트에 저장 (최대 45까지)
    triangular_numbers = [triangular_number(i) for i in range(1, 46)]

    # 삼중 반복문으로 3개의 삼각수를 선택해 합을 확인
    for i in triangular_numbers:
        for j in triangular_numbers:
            for k in triangular_numbers:
                if i + j + k == number:
                    return True
    return False


# 입력 받기
t = int(input())  # 테스트케이스의 개수
for _ in range(t):
    k = int(input())  # 자연수 K
    if is_eureka_number(k):
        print(1)
    else:
        print(0)
