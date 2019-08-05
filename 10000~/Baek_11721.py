inp = input()

while (len(inp) // 10) >= 1:
    print(inp[0:10])
    inp = inp[10:]
print(inp)