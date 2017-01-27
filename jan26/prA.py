def evaluate(lines_left, **kwargs):
    while lines_left:
        i = input()
        lines_left -= 1
        if i == '}':
            return lines_left
        elif i == '{':
            lines_left = evaluate(lines_left, **kwargs)
        else:
            split = i.split(' ')
            if split[0] == 'print':
                print(kwargs.get(split[1], 0))
            else:
                try:
                    value = int(split[2])
                except ValueError:
                    value = kwargs.get(split[2], 0)
                kwargs[split[0]] = value


if __name__ == "__main__":
    evaluate(int(input()))