def spy_game(nums):
    n = ""
    for i in range(len(nums)):
        if nums[i] == '0' or nums[i] == '7':
            n+=nums[i]
    if '007' in n:
        return True
    return False

nums = list(map(str, input().split()))
print(spy_game(nums))
