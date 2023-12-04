from collections import defaultdict

def part1(data):
    res = 0
    
    for line in data:
        win_count = get_win_count(line)
        if win_count > 0:
          res += 2 ** (win_count - 1)

    return res


def part2(data):
    counts = defaultdict(int)

    for i, line in enumerate(data):
        counts[i] += 1
        win_count = get_win_count(line)
        for idx in range(i + 1, i + 1 + win_count):
            counts[idx] += counts[i]

    return sum(list(counts.values()))


def get_win_count(line):
        _, numbers = line.split(': ')
        winning_numbers, my_numbers = [set(nums.strip().split()) for nums in numbers.split('|')]
        return len(winning_numbers.intersection(my_numbers))


def main():
    with open('./inputs/04.txt', 'r') as file:
        input_data = file.read().strip().split('\n')

    # Solve Part 1
    result_part1 = part1(input_data)
    print(f'Part 1: {result_part1}')

    # Solve Part 2
    result_part2 = part2(input_data)
    print(f'Part 2: {result_part2}')

if __name__ == '__main__':
    main()
