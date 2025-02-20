def trap_area(h, b1, b2):
    area = h * (b1 + b2)/2
    return area
h = int(input('Height:'))
b1 = int(input('Base, first value:'))
b2 = int(input('Base, second value:'))
area = trap_area(h, b1, b2)
print(f"Expected Output: {area}")