l = []
while True:
    try:
        l.append(int(input()))
    except EOFError:
        print(sum([l[i] < l[i+3] for i in range(len(l)-3)]))
        break
