
class SegmentTree:
    def __init__(self, low, high, values):
        self.low = low
        self.high = high
        self.diff = 0
        if low != high:
            self.left = SegmentTree(low, int((low + high)/2), values)
            self.right = SegmentTree(int((low + high)/ 2) + 1, high, values)
            self.value = min(self.left.value, self.right.value)
        else:
            self.value = values[self.low]
            self.left, self.right = None, None

    def add(self, low, high, value):
        if high >= self.low and low <= self.high:
            if low <= self.low and high >= self.high:
                self.diff += value
            elif self.low != self.high:
                self.left.add(low, high, value)
                self.right.add(low, high, value)
                self.value = min(self.left.value + self.left.diff, self.right.value + self.right.diff)

    def query(self, low, high):
        if low <= self.low and high >= self.high:
            return self.value + self.diff
        elif self.low == self.high:
            return 100000000000000000000000000000000000000000000
        elif high >= self.low and low <= self.high:
            return min(self.left.query(low, high), self.right.query(low, high)) + self.diff
        return 100000000000000000000000000000000000000000000

if __name__ == '__main__':
    size = int(raw_input())
    values = list(map(int, raw_input().split(' ')))
    tree = SegmentTree(0, size - 1, values)
    num_elements = int(raw_input())
    for _ in range(num_elements):
        params = list(map(int, raw_input().split(' ')))
        if len(params) == 2:
            if params[0] > params[1]:
                print(min(tree.query(params[0], size - 1), tree.query(0, params[1])))
            else:
                print(tree.query(*params))
        else:
            if params[0] > params[1]:
                tree.add(params[0], size - 1, params[2])
                tree.add(0, params[1], params[2])
            else:
                tree.add(*params)