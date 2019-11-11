num, max_num = map(int, input().split())
cards = list(map(int, input().split()))
sum = 0

for i in range(0, len(cards) - 2):
    for j in range(i + 1, len(cards) - 1):
        for k in range(j + 1, len(cards)):
            if cards[i] + cards[j] + cards[k] > max_num:
                continue
            else:
                sum = max(sum, cards[i] + cards[j] + cards[k])

print(sum)
