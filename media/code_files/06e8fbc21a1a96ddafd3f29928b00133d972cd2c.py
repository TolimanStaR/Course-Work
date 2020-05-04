import math

n = int(input())

f = []

s_l_t = 0
l_t = 0
l_s = 0
s_t = 0
s_, l_, t_ = 0, 0, 0

for i in range(pow(2, pow(2, n))):
    num = str(bin(i))[2:]
    v = '0' * max(0, pow(2, n) - len(num)) + num
    f.append(v)


def polynom(vector):
    matrix = [[0] * len(vector) for i in range(len(vector))]
    matrix[0] = [int(x) for x in vector]

    for i in range(1, len(vector)):
        for j in range(len(vector) - i):
            matrix[i][j] = matrix[i - 1][j] ^ matrix[i - 1][j + 1]

    return [x[0] for x in matrix]


for v in f:
    s, l, t = 0, 0, 0

    if v == v[::-1]:
        s = True
        s_ += 1

    if v[0] == '1':
        t = True
        t_ += 1

    k = polynom(v)
    cnt = k[0]

    for i, x in enumerate(k):
        if i != 0:
            if x == 1 and math.log2(i) % 1 == 0:
                cnt += 1

    if cnt == k.count(1):
        l = True
        l_ += 1

    if l and s and t:
        s_l_t += 1

    if l and s:
        l_s += 1

    if s and t:
        s_t += 1

    if l and t:
        l_t += 1

print(f'L S T: {s_l_t}')
print(f'L S: {l_s}')
print(f'L T: {l_t}')
print(f'S T: {s_t}')

print(s_, l_, t_)
