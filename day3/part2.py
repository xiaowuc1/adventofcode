def gen(l, i, x):
    r = [[], []]
    for elem in l:
        r[int(elem[i])].append(elem)
    if len(r[0]) == len(r[1]):
        return r[x]
    return r[x == (len(r[1]) > len(r[0]))]

def f(l, g, x):
    for j in range(len(l[0])):
        l = g(l, j, x)
        if len(l) == 1:
            break
    return int(l[0], 2)

l = []
while True:
    try:
        l.append(input())
    except EOFError:
        break
print(f(l, gen, 1) * f(l, gen, 0))
