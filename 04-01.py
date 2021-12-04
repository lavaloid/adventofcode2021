with open('04-input.txt') as f:
    f_split = f.read().split()

order = f_split[0].split(',')
boards = f_split[1:]
board_state = [False]*(len(f_split) - 1)

def board_is_finished(idx):
    for i in range(5):
        offset = idx * 25
        # row
        if all(board_state[offset + i * 5: offset + i * 5 + 5]):
            return True

        # column
        if all(board_state[offset + i : offset + 25 : 5]):
            return True
    
    return False

def perform_action(num):
    for i in range(len(boards) // 25):
        for j in range(25):
            if boards[i * 25 + j] == num:
                board_state[i * 25 + j] = True
                break

        if board_is_finished(i):
            return i

    return None

finished_board = 0
finished_num = 0
for num in order:
    result = perform_action(num)
    if result != None:
        finished_board = result
        finished_num = int(num)
        break

unmarked_total = 0
for i, cell in enumerate(boards[finished_board * 25: finished_board * 25 + 25]):
    if not board_state[finished_board * 25 + i]:
        unmarked_total += int(cell)

print(finished_num * unmarked_total)
