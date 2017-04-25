n, in_arr = int(input()), list(map(int, input().split(' ')))
num_values = len(in_arr)
cache = [None] * num_values
for i in range(num_values):
    index = num_values - i - 1
    cache[index] = 1 if index + 1 == num_values else max(cache[other_index] + 1 if in_arr[other_index] > in_arr[index] else 1 for other_index in range(index + 1, num_values))
print(cache[0])
