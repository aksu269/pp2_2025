def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 3:
            if nums[i + 1] == 3:
                return True
    return False
nums = [3, 1, 3]
print(has_33(nums))
