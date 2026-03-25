#1920문제
import sys; 
input = sys.stdin.readline
N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
for x in map(int, input().split()):
    lo, hi, found = 0, N-1, False
    while lo <= hi:
        mid = (lo+hi)//2
        if A[mid]==x: 
            found=True
            break
        elif A[mid]<x: 
            lo=mid+1
        else: hi=mid-1
    print(1 if found else 0)