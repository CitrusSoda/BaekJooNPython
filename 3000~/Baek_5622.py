alpha_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
inp = input()
count = 0

for i in range(len(inp)):
    for j in alpha_list:
        if inp[i] in j:
            num = alpha_list.index(j) + 3
            count += num

print(count)
