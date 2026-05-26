nums=[]
cnt_3=0
cnt_5=0

for _ in range(10):
    nums.append(int(input()))

for x in nums:
    if x%3==0:
        cnt_3+=1
    if x%5==0:
        cnt_5+=1

print(f"{cnt_3} {cnt_5}")