
class SegmentTree:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        if low != high:
            self.left = SegmentTree(low, int((low + high)/2))
            self.right = SegmentTree(int((low + high)/ 2) + 1, high)
            self.value = max(self.left.value, self.right.value)
        else:
            self.value = 0
            self.left, self.right = None, None

    def add(self, key, value):
        if self.low == self.high:
            self.value += value
        else:
            if key >= self.right.low:
                self.right.add(key, value)
            else:
                self.left.add(key, value)
            self.value = max(self.left.value, self.right.value)

    def query(self, low, high):
        # print("hit", self.low, self.high)
        if low <= self.low and high >= self.high:
            return self.value
        elif self.low == self.high:
            return 0
        elif high >= self.low and low <= self.high:
            return max(self.left.query(low, high), self.right.query(low, high))
        return 0


if __name__ == '__main__':
    accounts, transactions = map(int, raw_input().split(' '))
    tree = SegmentTree(0, accounts - 1)
    for _ in range(transactions):
        t_name, p_0, p_1 = raw_input().split(' ')
        if t_name == "ADD":
            tree.add(int(p_0), int(p_1))
        else:
            # print("queried", p_0, p_1)
            print(tree.query(int(p_0), int(p_1)))