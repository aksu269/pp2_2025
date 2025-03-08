string = 'AksU'
cnt_lower = 0
cnt_upper = 0
for x in string:
    if x.islower():
        cnt_lower += 1
    else:
        cnt_upper += 1
print(f"Number of lower case letters: {cnt_lower}.")
print(f"Number of upper case letters: {cnt_upper}.")