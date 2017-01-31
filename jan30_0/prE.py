def lcm(x, y):
   if x > y:
       z = x
   else:
       z = y

   while(True):
       if((z % x == 0) and (z % y == 0)):
           lcm = z
           break
       z += 1

   return lcm


if __name__ == '__main__':
    rows, columns = [int(i) - 1 for i in input().split(' ')]
    direction = input()
    movements = lcm(rows, columns)
    if movements / rows % 2 == 1:
        direction = direction.replace('N', 'S') if 'N' in direction else direction.replace("S", "N")
    if movements / columns % 2 == 1:
        direction = direction.replace('E', 'W') if 'E' in direction else direction.replace("W", "E")
    print(direction)
    # if direction == 'NE':
    #     x = columns
    #     y = 0
    #     direction = "SW"
    # elif direction == 'NW':
    #     x = 0
    #     y = 0
    #     direction = 'SE'
    # elif direction == 'SE':
    #     x = 0
    #     y = rows
    #     direction = 'NW'
    # else:
    #     x = columns
    #     y = rows
    #     direction = 'NE'
    #
    # def in_hole():
    #     return (x == 0 or x == columns) and (y == 0 or y == rows)
    #
    # while True:
    #     if 'E' in direction:
    #         x += 1
    #     else:
    #         x -= 1
    #     if 'S' in direction:
    #         y += 1
    #     else:
    #         y -= 1
    #     if in_hole():
    #         break
    #     if x == 0:
    #         direction = direction.replace('W', 'E')
    #     elif x >= columns:
    #         direction = direction.replace('E', 'W')
    #     if y == 0:
    #         direction = direction.replace('N', 'S')
    #     elif y == rows:
    #         direction = direction.replace('S', 'N')
    # if x == 0:
    #     if y == 0:
    #         print('NW')
    #     else:
    #         print('SW')
    # else:
    #     if y == 0:
    #         print('NE')
    #     else:
    #         print('SE')
