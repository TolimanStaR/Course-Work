n, t = map(int, input().split())
a = list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(t)]

pref = [0] * n
pref[0] = a[0]

for i in range(1, n):
	pref[i] += a[i] + pref[i - 1]
	
for i in range(t):
	print(pref[s[i][1]] - pref[s[i][0]])
	