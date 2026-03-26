#2343 문제
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lessons = list(map(int, input().split()))
lo, hi = max(lessons), sum(lessons)
ans = hi
while lo <= hi:
    mid = (lo + hi) // 2
    #mid는 무조건 레슨의 최소값이상
     # check: mid 크기로 M장 이내 가능?
    count, total = 1, 0
    #이진 탐색을 하면서 ans값 찾기
    for l in lessons:
    #한 블루레이를 다 채우면 다음 블루레이 채우기
        if total + l > mid:#만약 강의 목록을 더하면 블루레이 값보다 커지면 
            count += 1
            total = 0#블루레이 1개를 썼고 이제 다음 불루레이 채우기
        total += l#강의 목록들을 더한다
    #기존의 블루레이 크기로 간능하면 탐색값을 중간값 미만으로 
    if count <= M: # 가능!
        ans = mid
        hi = mid - 1
    else: # 불가능
       lo = mid + 1
print(ans)