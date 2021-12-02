x = 0
y = 0
aim = 0
while True:
    try:
        s = input().split()
        if s[0] == "forward":
            x += int(s[1])
            y += int(s[1]) * aim
        elif s[0] == "down":
            aim += int(s[1])
        else:
            assert s[0] == "up"
            aim -= int(s[1])
    except EOFError:
        print(x*y)
        break
