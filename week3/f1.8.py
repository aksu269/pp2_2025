def spy_game(nums):
    temp = ''
    for x in nums:
        if x == 0:
            temp += '0'
        elif x == 7:
            temp += '7'
    if ('007' in temp):
        return True
    return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0])) 