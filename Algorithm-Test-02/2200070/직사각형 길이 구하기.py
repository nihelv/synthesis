t=int(input())

for num in range(1, t+1):
    n1=list(map(int, input().split()))
    for s in n1:
        if n1.count(s) != 2 :
            print(f'#{num} {s}')
            break

# 예외지정에 좀 헤맴
# 100개 중에 94개가 맞았다고 하니 더 상상이 안 가더라.. 해당되는 6개가 대체 뭐냐고
# s=s=s 인 정사각형일 때 한번 출력하고 브레이크 걸어야 했음