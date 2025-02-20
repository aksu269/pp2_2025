import datetime
import math
def diff(a, b):
    dif = abs(a - b)
    return dif.total_seconds()
a = datetime.datetime(2025, 4, 4)
b = datetime.datetime(2025, 5, 5)
print(diff(a, b))