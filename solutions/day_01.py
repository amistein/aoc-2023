def part1(data):
    res = 0
    for line in data:
        s = ''
        for c in line:
            if c.isnumeric():
                s += c
                break

        for c in reversed(line):
            if c.isnumeric():
                s += c
                break

        res += int(s)

    return res

def part2(data):
    table = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    tokens = list('123456789') + list(table.keys())
    reverse_tokens = list('123456789') + [k[::-1] for k in table.keys()]
    res = 0

    for line in data:
        idx = len(line)
        r_line = line[::-1]
        first_token = last_token = None

        for t in tokens:
            curr = line.find(t)
            if curr != -1 and curr < idx:
                idx = curr
                first_token = t if len(t) == 1 else str(table[t])

        idx = len(line)
        for t in reverse_tokens:
            curr = r_line.find(t)
            if curr != -1 and curr < idx:
                idx = curr
                last_token = t if len(t) == 1 else str(table[t[::-1]])

        res += int(first_token + last_token)

    return res
            

def main():
    with open('./inputs/01.txt', 'r') as file:
        input_data = file.read().strip().split('\n')

    # Solve Part 1
    result_part1 = part1(input_data)
    print(f'Part 1: {result_part1}')

    # Solve Part 2
    result_part2 = part2(input_data)
    print(f'Part 2: {result_part2}')

if __name__ == '__main__':
    main()
