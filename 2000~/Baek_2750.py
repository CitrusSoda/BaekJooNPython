case = int(input())
num_list = []

for i in range(case):
    num = int(input())
    num_list.append(num)

sort = sorted(num_list)
for i in sort:
    print(i)