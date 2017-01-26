def fail():
    print("Invalid")
    exit(0)

if __name__ == "__main__":
    nums = input()
    num_names, num_changes = nums.split(' ')
    names = {}
    for i in range(int(num_names)):
        in_str = input()
        names[in_str] = in_str
    for i in range(int(num_changes)):
        doer, change_from, change_to = input().split(' ')
        if doer not in names or change_from not in names:
            fail()
        if change_from != change_to and change_to in names:
            fail()
        names[change_to] = names.pop(change_from)
    for key in sorted(names.keys()):
        print('{}:{}'.format(key, names[key]))

