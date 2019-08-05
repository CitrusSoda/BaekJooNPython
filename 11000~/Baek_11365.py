while True:
    password = input()

    if password == 'END':
        break

    rev_arr = list(reversed(password))
    print("".join(rev_arr))