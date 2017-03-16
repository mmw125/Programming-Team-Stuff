import math
diameter, height, drink_speed, fill_speed = map(int, input().split(' '))
print("NO" if (drink_speed / (diameter / 2) / (diameter / 2) / math.pi) < fill_speed else "YES\n" + str(height / ((drink_speed / (diameter / 2) / (diameter / 2) / math.pi) - fill_speed)))
