# 3273 두 수의 합
n = int(input())
a = list(map(int, input().split()))
x=int(input())

seen=set()
count=0
for num in a:
    if x-num in seen:
        count+=1
    seen.add(num)
print(count)
