case = int(input())
count = 0

for i in range(case):
    check_list = []
    alpha_list = [0] * 26

    word = input()

    for j in range(len(word)):
        if j == 0:
            check_list.append(word[j])
        elif word[j - 1] == word[j]:
            continue
        else:
            check_list.append(word[j])

    for j in range(len(check_list)):
        alpha_list[ord(check_list[j]) - 97] += 1

    if max(alpha_list) == 1:
        count += 1

print(count)
