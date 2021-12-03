l = []
while True:
    try:
        l.append(input())
    except EOFError:
        break
r = [0, 0]
for j in range(len(l[0])):
    r[0] *= 2
    r[1] *= 2
    r[2*sum(int(y[j]) for y in l) > len(l)] += 1
print(r[0] * r[1])
