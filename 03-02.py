with open('03-input.txt') as f:
    f_split = f.read().split('\n')[:-1]

f_split.sort()
length = len(f_split)

def find_count(idx, l, r):
    # i guess i could binary search but im lazy
    for i in range(l, r + 1):
        if f_split[i][idx] == '1':
            return i - l, r - i + 1
    return r, 0

oxygen_l = 0
oxygen_r = length - 1
co2_l = 0
co2_r = length - 1

oxygen_b = None
co2_b = None

# split first digit
zero_0, one_0 = find_count(0, 0, length - 1)
if zero_0 <= one_0:
    oxygen_l = zero_0
    co2_r = zero_0 - 1
elif zero_0 > one_0:
    oxygen_r = zero_0 - 1
    co2_l = zero_0

# second digit onwards, oxygen
for idx in range(1, len(f_split[0])):
    zero, one = find_count(idx, oxygen_l, oxygen_r)

    if zero <= one:
        oxygen_l = oxygen_l + zero
    else:
        oxygen_r = oxygen_l + zero - 1

    if oxygen_l == oxygen_r:
        oxygen_b = f_split[oxygen_l]

# second digit onwards, co2
for idx in range (1, len(f_split[0])):
    zero, one = find_count(idx, co2_l, co2_r)

    if zero <= one:
        co2_r = co2_l + zero - 1
    else:
        co2_l = co2_l + zero

    if co2_l == co2_r:
        co2_b = f_split[co2_l]

# binary --> decimal
oxygen = 0
co2 = 0
for i in range(len(oxygen_b)):
    oxygen *= 2
    co2 *= 2

    oxygen += (oxygen_b[i] == '1')
    co2 += (co2_b[i] == '1')

print(oxygen * co2)
