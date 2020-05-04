n, t = map(int, input().split())
nums = set(map(int, input().split()))
years = list(map(int, input().split()))
for i in years:
    if i in nums:
        print("Yes")
    else:
        print("No")
