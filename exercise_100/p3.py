import math
for i in range(10001):
        x=math.sqrt(i + 100)
        y=math.sqrt(i + 268)
        if (x - int(x) == 0) and (y - int(y) == 0):
                print(i)
