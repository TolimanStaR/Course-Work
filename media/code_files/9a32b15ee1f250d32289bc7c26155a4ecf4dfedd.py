n = int(input())
s = input()
min = 'z'
array = []
for i in range(n):
    if min > s[i]:
        array.append(s[i])
        min = s[i]
    else:
        array.append(min)

for k in range(n):
    if array[k] == s[k]:
        print("A")
    else:
        print("H")