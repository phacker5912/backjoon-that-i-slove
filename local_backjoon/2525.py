a, b = map(int, input().split())
c = int(input())

c += b
a += c // 60
b = c % 60

if a > 23:
    a -= 24

print(a, b)