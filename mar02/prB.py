import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def scale(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def rotate(self, theta):
        math.hypot(self.x, self.y)
        cur_theta = math.atan2(y, x)


if __name__ == '__main__':
    start_x, start_y, direction_x, direction_y ,a, b, c, d = map(int, input().split(' '))
