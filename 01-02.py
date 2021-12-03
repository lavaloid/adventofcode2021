with open('01-input.txt') as f:
    f_split = f.read().split()

count = 0

for idx, _ in enumerate(f_split[:-3]):
    if int(f_split[idx]) < int(f_split[idx + 3]):
        count += 1

print(count)
