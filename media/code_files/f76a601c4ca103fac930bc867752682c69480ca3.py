n, t = map(int, input().split())
a = list(map(int, input().split()))
r = list(map(int, input().split()))

for num in r:
	if num in a:
		print("Yes")
	else:
		print("No")