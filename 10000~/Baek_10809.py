a = input()
count = [-1] * 26

for i in range(len(a)):
    #알파벳의 위치를 반환한다. (아스키코드 이용)
    if count[ord(a[i]) - 97] != -1:
        continue
    else:
        count[ord(a[i]) - 97] = i

for i in range(26):
    print(count[i])