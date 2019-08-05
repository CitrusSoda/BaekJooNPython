num = int(input())

a = map(int, input().split())
li = list(a)
max_li = max(li)

for i in range(num):
    li[i] = li[i] / max_li * 100

sum = 0
for i in range(num):
    sum = sum + li[i]
print(sum / num)