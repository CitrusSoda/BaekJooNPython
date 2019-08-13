num = int(input())
a = 0

while num > 0:
    num -= a
    a += 1

num = num + a - 1

if a % 2 == 1:
    print(num,'/',a - num, sep='')
else:
    print(a - num,'/',num,sep='')