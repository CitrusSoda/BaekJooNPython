num = []
for i in range(10):
    num.append(int(input()) % 42)
# set을 이용하면 중복을 제거할 수 있다.
num_set = list(set(num))

print(len(num_set))