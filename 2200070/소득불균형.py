t=int(input())

for num in range(1, t+1):
    n=int(input())
    result=0
    p=list(map(int, input().split()))
    a=int(sum(p) / len(p))
    for elem in p:
        if elem <= a:
            result += 1
    
    print(f'#{num} {result}')


# 예제 케이스 2번: 세상은 썩었어 ㅎㅎ
# 구상한 대로 잘 풀림