
if __name__ == '__main__':
    num_cards = int(input())
    half = int(num_cards / 2)
    cards_to_read = half
    if num_cards % 2 == 1:
        half += 1
    start = [input() for i in range(half)]
    for i in range(cards_to_read):
        print(start[i])
        print(input())
    if half != cards_to_read:
        print(start[cards_to_read])