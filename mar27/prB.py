import sys
sys.setrecursionlimit(50001)
if __name__ == '__main__':
    width, height = map(int, input().split(' '))
    map = list()
    start_location = None
    for i in range(height):
        in_str = input()
        if "P" in in_str:
            start_location = i, in_str.index("P")
        map.append(in_str)

    visited_list = [[False] * width for _ in range(height)]
    gold = 0

    def navigate(x, y):
        global gold
        if x < 0 or x >= width or y < 0 or y >= height:
            return
        if visited_list[y][x]:
            return
        visited_list[y][x] = True
        if map[y][x] == "G":
            gold += 1
        if map[y][x] == "T" or map[y][x] == "#":
            return
        if map[y - 1][x] == "T" or map[y + 1][x] == "T" or map[y][x + 1] == "T" or map[y][x - 1] == "T":
            return
        navigate(x - 1, y)
        navigate(x + 1, y)
        navigate(x, y - 1)
        navigate(x, y + 1)
    navigate(start_location[1], start_location[0])
    print(gold)
