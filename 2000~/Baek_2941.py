cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alpha = input()

for i in cro:
    alpha = alpha.replace(i, '*')

print(len(alpha))