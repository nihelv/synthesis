import sys
sys.stdin=open('input.txt', 'r')

t=int(input())
# 테스트 케이스 수
for _ in range(1, t+1):
    #문제에서 1번부터 출력하기 요구하므로 1부터 t+1까지의 리스트를 만들고
    n=int(input())
    #카드 수를 입력하고
    d=list(input().split())
    #카드 구성을 리스트로 받는다
    d1=[]
    d2=[]
    d3=[]
    #d1, d2는 반반씩 담을 거. d3은 한장씩 뽑을 거
    for c in range(n):
        # 여기에서 led(d)를 써야하나 했는데 그냥 n이랑 그게 그거더라
        if c < n // 2:
            d1.append(d[c])
            #c를 인덱스로 하는 리스트 d의 요소를 나눠서 넣을건데
            #먼저 c가 n을 2로 나눈 것의 몫보다 작으면 d1에 넣어주고

        else:
            #c가 n을 2로 나눈 몫보다 큰데
            if n % 2 == 1:
                #n이 홀수면
                d1.append(d[c])
                #d1에 한번 더 넣어주고
            d2.append(d[c])
            #나머지 남은 거를 d2에 넣어준다
            #여기까지 절반 나누기

    while True:
        #여기서 트루를 쓰는게 맞나? 영 모르겠네
        if len(d1) != 0:
            # d1 리스트의 길이가 0이 아니면
            d3.append(d1.pop(0))
            # 먼저 d1 맨 앞자리에서 카드를 뽑아서 d3에 넣고
            try : d3.append(d2.pop(0))
            except : continue
            # 다음으로 d2 맨 앞자리에서 카드를 뽑아서 d3에 넣는데
            # n이 홀수일 경우 100% 빈 리스트(d2가 먼저 바닥남)에서 팝 못한다고 오류가 날 것이기 때문에
            # try문을 사용해서 d2에 뭐가 있으면 계속 뽑고 오류를 뱉거든 걍 넘어가거라 하고 명령을 내린다
            # try문 처음써봄
        else:
            print(f'#{_}', *d3)
            break
        # d1리스트의 길이가 0이면 프린트하고 브레이크

# 처음에 이렇게 이렇게 풀면 되겠다! 하고 계획을 짠 건 맞았는데
# 계속 원하는 대로 출력이 안되어서 조금씩 조금씩 디테일을 다듬었으나 8개 케이스 중 5개 정답이라고 함
# 입력 예시 세개는 맞았다고 빼애앵
# 힝구 뭐가 빠졌느냐
        

    


