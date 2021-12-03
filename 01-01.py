with open('01-input.txt') as f:
    f_split = f.read().split()

count = 0

prev = int(f_split[0])
for current_str in f_split[1:]:
    current = int(current_str)
    if prev < current:
        count += 1
    prev = current

print(count)
