n, t = map(int, input().split())
array = list(map(int, input().split()))
usual_array = [0]
s = 0
for i in range(n):
    s += array[i]
    usual_array.append(s)

difichentos_array = [0]*(n+1)
ans_arr = []
for req in range(t):
    r, x, y = map(int, input().split())
    if r == 0:
        for i in range(x+1, n+1):
            difichentos_array[i] += y - array[x]

    else:
        ans = usual_array[y+1] - usual_array[x] + difichentos_array[y+1] - difichentos_array[x]
        ans_arr.append(ans)

print(*ans_arr)

