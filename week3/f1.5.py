from itertools import permutations 
def perms(string)
    perm = permutations(string)
    for i in perm:
        print(i)
string = input()
perms(string)
