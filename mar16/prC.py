import sys

class SegmentTree:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.diff = 0
        self.initd = False

    def initialize(self):
        self.initd = True
        if self.low != self.high:
            self.left = SegmentTree(self.low, int((self.low + self.high)/2))
            self.right = SegmentTree(int((self.low + self.high)/ 2) + 1, self.high)
            self.val = 0
            self.max_size = 0
        else:
            self.max_size = 1
            self.val = 0
            self.left, self.right = None, None

    def add(self, low, high, value):
        if not self.initd:
            self.initialize()
        if high >= self.low and low <= self.high:
            if low <= self.low and high >= self.high:
                self.diff += value
            elif self.low != self.high:
                self.left.add(low, high, value)
                self.right.add(low, high, value)
                self.val = max(self.left.value(), self.right.value())
                self.max_size = (self.left.max_size if self.left.value() == self.value else 0
                            + self.right.max_size if self.right.value() == self.value else 0)

    def value(self):
        return self.val + self.diff

    def __str__(self):
        return '' if not self.initd else '\n'.join((' '.join((str(self.value()), str(self.low), str(self.high))), str(self.left), str(self.right)))


if __name__ == '__main__':
    for _ in range(int(input())):
        tree = SegmentTree(-1000000, 1000000)
        blocks = []
        for __ in range(int(input())):
            string = input()
            x_0, x_1, y_0, y_1, diff = map(int, string.split(' '))
            mul_val = 1 if x_0 < x_1 else -1
            blocks.append((x_0, y_0, y_1, diff * mul_val))
            blocks.append((x_1, y_0, y_1, -diff * mul_val))
        blocks.sort()
        last_block_x = None
        max_val = 0
        max_size = 0
        for block in blocks:
            if last_block_x is None or block[0] == last_block_x:
                pass
            else:
                # print(block[0])
                if tree.value() > max_val:
                    max_size = 0
                    max_val = tree.value()
                if tree.value() == max_val:
                    max_size += tree.max_size * (block[0] - last_block_x)
            tree.add(block[1], block[2], block[3])
            print(tree)
            # print("max val", max_val)
            last_block_x = block[0]
        print("FINAL", max_val, max_size)