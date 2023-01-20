T=int(input())

for case in range(1, T+1):
    p=[]
    for b in input():
        if b == 'b':
            p.append('d')
        elif b == 'd':
            p.append('b')
        elif b == 'p':
            p.append('q')
        elif b == 'q':
            p.append('p')

    r=list(reversed(p))
    print(f'#{case}', ' ', *r, sep='')


# 자꾸 오답처리 되어서 내가 뭘 잘못 계산했나 했더니
# f스트링에 # 빠져있었다. 이럴 때 넘 빡침.. r로 출력되는 글자만 보다가