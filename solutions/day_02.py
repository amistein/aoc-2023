from collections import defaultdict

def part1(data):
    maxs = {'red': 12, 'green': 13, 'blue': 14}
    res = 0

    for line in data:
        prefix, game_data = line.split(': ')
        found_over = False
        hands = game_data.split('; ')
        for hand in hands:
            if found_over:
                break

            colors = hand.split(', ')
            for item in colors:
                count, color = item.split(' ')
                if int(count) > maxs[color]:
                    found_over = True
                    break
        
        if not found_over:
            res += int(prefix.split(' ')[1])

    return res


def part2(data):
    res = 0

    for line in data:
        d = defaultdict(int)
        _, game_data = line.split(': ')
        hands = game_data.split('; ')
        for hand in hands:
            colors = hand.split(', ')
            for item in colors:
                count, color = item.split(' ')
                d[color] = max(d[color], int(count))

        res += d['red'] * d['green'] * d['blue']

    return res

def main():
    with open('./inputs/02.txt', 'r') as file:
        input_data = file.read().strip().split('\n')

    # Solve Part 1
    result_part1 = part1(input_data)
    print(f'Part 1: {result_part1}')

    # Solve Part 2
    result_part2 = part2(input_data)
    print(f'Part 2: {result_part2}')

if __name__ == '__main__':
    main()
