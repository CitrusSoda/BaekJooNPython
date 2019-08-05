a = int(input())
b = int(input())
c = int(input())

prd = a * b * c

num = []

while prd != 0:
    num.append(prd % 10)
    prd = prd // 10

count = 0
for i in range(10):
    for j in range(len(num)):
        if num[j] == i:
            count += 1
    print(count)
    count = 0