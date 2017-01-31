class Obstruction:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def __str__(self):
        return '{}, {}'.format(self.start, self.end)

if __name__ == '__main__':
    while True:
        fence_length = float(input())
        if fence_length == -1:
            exit(0)
        obstructions = []
        while True:
            x, y = [float(i) for i in input().split(' ')]
            if x > y:
                break
            obstructions.append(Obstruction(x, y))
        st_sor = sorted(obstructions, key=Obstruction.get_start)
        end_sor = sorted(obstructions, key=Obstruction.get_start)
        depth = 0
        st_i = 0
        end_i = 0
        length = 0
        position = 0
        for index in range(len(st_sor) * 2):
            start_pos = st_sor[st_i].start if len(st_sor) > st_i else fence_length
            if start_pos <= end_sor[end_i].end:
                if depth == 0:
                    length += st_sor[st_i].start - position
                depth += 1
                position = st_sor[st_i]
                st_i += 1
            else:
                depth -= 1
                position = end_sor[end_i].start
                end_i += 1
        length += position - length
        print('The total planting length is {}'.format(length))
