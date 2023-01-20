T = int(input())
# T=1

for test_case in range(1, T + 1):
    tem={}
    test_num=int(input())
    # test_num=1
    input_v=list(map(int, input().split()))
    for num in input_v:
        o=input_v.count(num)
        tem[o]=num

    print(f'#{test_num} {tem.get(max(tem))}')


# 딕셔너리 해서 푸는 문제가 맞나?
# 키가 빈도수, 점수가 밸류로 해서 max로 키의 최대값 리턴, 해당 키의 밸류 출력
# 점수가 키인게 보기에 나을지도 모르지만 내가 딕셔너리 보고 눈으로 산출하는게 아니니까..