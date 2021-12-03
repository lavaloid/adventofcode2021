with open('02-input.txt') as f:
    f_split = f.read().split('\n')[:-1]

pos = 0
depth = 0
for s in f_split:
    instruction = s.split()
    if instruction[0] == 'forward':
        pos += int(instruction[1])
    elif instruction[0] == 'up':
        depth -= int(instruction[1])
    elif instruction[0] == 'down':
        depth += int(instruction[1])

print(pos * depth)
