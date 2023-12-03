def part1(data):
    res = 0
    for i, line in enumerate(data):
        numbers = get_numbers(line)

        for s, e, n in numbers:
            prev_line = data[i - 1] if i > 0 else ''
            next_line = data[i + 1] if i < len(data) - 1 else ''
            is_symbol = lambda x: x != '.' and not x.isalnum()
            prev_char_symbol = False if s < 0 else is_symbol(line[s])
            next_char_symbol = False if e == len(line) else is_symbol(line[e])
            contains_symbol = lambda x: len([c for c in x if is_symbol(c)]) != 0
            if prev_char_symbol or next_char_symbol or contains_symbol(prev_line[max(s, 0):e + 1]) or contains_symbol(next_line[max(s, 0):e + 1]):
                res += n

    return res


def part2(data):
    res = 0
    for i, line in enumerate(data):
        numbers1 = get_numbers(line)
        numbers2 = [] if i == 0 else get_numbers(data[i - 1])
        numbers3 = [] if i == len(data) - 1 else get_numbers(data[i + 1])
        for idx in range(len(line)):
            if line[idx] == '*':
                same_line = [n for s, e, n in numbers1 if s == idx or e == idx]
                others = [n for s, e, n in numbers2 + numbers3 if s <= idx and e >= idx]
                all_adj = same_line + others

                if len(all_adj) == 2:
                    res += (all_adj[0] * all_adj[1])

    return res

def get_numbers(s):
    i = 0
    res = []

    while i < len(s):
        start = None
        curr_num = []
        if s[i].isnumeric():
            start = i
            while i < len(s) and s[i].isnumeric():
                curr_num.append(s[i])
                i += 1
            res.append((start - 1, i, int(''.join(curr_num))))
        else:
            i += 1

    return res

def main():
    with open('./inputs/03.txt', 'r') as file:
        input_data = file.read().strip().split('\n')

    # Solve Part 1
    result_part1 = part1(input_data)
    print(f'Part 1: {result_part1}')

    # Solve Part 2
    result_part2 = part2(input_data)
    print(f'Part 2: {result_part2}')

if __name__ == '__main__':
    main()
