T=int(input())
# T=1

for case in range(1, T+1):
    c=list(map(int, input().split()))
    f=[]
    s=[]
    result=0

    for i in range(len(c)):
        v=c[i]
        if i == 0:
            f.append(v)
        elif i % 2 == 1:
            s.append(v)
        else:
            f.append(v)

    for n in f:
        n1 = n * 2
        result += n1

    if 10-((result + sum(s))%10)==10:
        N=0
    else:
        N=10-((result + sum(s))%10)
        
    print(f'#{case} {N}')


# for, for, if 다시 for...
# 기이이이러요