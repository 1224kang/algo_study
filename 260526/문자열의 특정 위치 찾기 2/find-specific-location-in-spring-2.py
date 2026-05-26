arr=["apple","banana","grape","blueberry","orange"]
str=input()
count=0
included=[]

for x in arr:
    if x[2]==str or x[3]==str:
        count+=1
        included.append(x)

for word in included:
    print(word)
print(count)


