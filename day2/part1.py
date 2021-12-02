x = 0
y = 0
aim = 0
while True:
    try:
        s = input().split()
        if s[0] == "forward":
            x += int(s[1])
        elif s[0] == "down":
            y += int(s[1])
        else:
            assert s[0] == "up"
            y -= int(s[1])
    except EOFError:
        print(x*y)
        break
