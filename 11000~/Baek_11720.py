case = int(input())
num = int(input())

count = 0
sum = 0

while count != case:
    sum += num %10
    num = num //10
    count += 1

print(sum)