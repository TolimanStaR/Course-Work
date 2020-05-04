n, t = map(int, input().split())
nums = set(map(int, input().split()))
years = set(map(int, input().split()))
for i in years:
    if i in nums:
        print("Yes")
    else:
        print("No")
