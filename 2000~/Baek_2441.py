num = int(input())

for i in range(num):
    for none in range(i):
        print(' ',end='')
    for star in range(num - i):
        print('*',end='')
    print('\n', end='')
