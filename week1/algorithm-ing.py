n=int(input())
scores=list(map(int,input().split()))
sum=0
max = scores[0]


for i in range(len(scores)):
     if scores[i]>max:
         max=scores[i]

for i in range(len(scores)):
    scores[i]=scores[i]/max*100
    sum+=scores[i]

print(float(sum/n))