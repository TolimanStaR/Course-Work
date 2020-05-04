n = int(input())
s = str(input())

p = [s[0]]

for i in range(1, n):
	p.append(min(p[i - 1], s[i - 1]))

for i in range(n):
	print('A' if p[i] >= s[i] else 'H')
