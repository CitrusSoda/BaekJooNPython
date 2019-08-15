alpha = input().upper()
alpha_count = [0] * 26

for i in range(len(alpha)):
    alpha_count[ord(alpha[i]) - 65] += 1

if alpha_count.count(max(alpha_count)) >= 2:
    print('?')
else:
    print(chr(alpha_count.index(max(alpha_count)) + 65))
