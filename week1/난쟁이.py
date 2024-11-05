from itertools import combinations

# 아홉 난쟁이의 키를 입력받습니다.
heights = [int(input()) for _ in range(9)]

# 9명 중 7명을 선택하는 모든 조합을 탐색합니다.
for combo in combinations(heights, 7):
    if sum(combo) == 100:
        # 키가 100이 되는 일곱 난쟁이를 출력합니다.
        for height in sorted(combo):
            print(height)
        break
