import math
def d_to_r(d):
    r = d * math.pi / 180
    return r 
d = int(input("Input degree:"))
g = d_to_r(d)
print(f"Output radian: {g:.6f}")