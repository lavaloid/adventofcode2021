with open('03-input.txt') as f:
    f_split = f.read().split('\n')[:-1]

zero_counts = [0] * len(f_split[0])
for b in f_split:
    for i, c in enumerate(b):
        zero_counts[i] += int(c == '0')

length = len(f_split)

gamma = 0
epsilon = 0
for i in zero_counts:
    gamma *= 2
    epsilon *= 2

    if length - i < i:
        gamma += 1
    else:
        epsilon += 1

print(gamma * epsilon)
