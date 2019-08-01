#조건 : 1 <= A, B와 C는 <= 100
x, y, z = map(int, input().split())
num_array = [x, y, z]
temp = 0
#정렬 -----------------------------------
for j in range (2):
    for i in range(2):
        if num_array[i] > num_array[i+1]:
            temp = num_array[i + 1]
            num_array[i + 1] = num_array[i]
            num_array[i] = temp
#중간 값 출력 ----------------------------
print(num_array[1])
