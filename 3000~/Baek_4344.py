case = int(input())
#리스트 만들기
for i in range(case):
    num = map(int, input().split())
    li = list(num)
    #첫 수(개수)
    first_num = li[0]
    #평균 계산
    sum = 0
    for j in range(len(li) - 1):
        sum += li[j + 1]
    average = sum / (len(li) - 1)
    #평균과 비교
    more = 0
    for k in range(len(li) - 1):
        if li[k + 1] > average:
            more += 1
    #비율, 소숫점 3번째자리까지
    rate = more / first_num * 100
    print(format(rate,".3f"), end='%\n')