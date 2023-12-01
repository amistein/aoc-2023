def part1(data):
    # Your solution for Part 1 goes here
    pass

def part2(data):
    # Your solution for Part 2 goes here
    pass

def main():
    with open('./inputs/01.txt', 'r') as file:
        input_data = file.read().strip()

    # Solve Part 1
    result_part1 = part1(input_data)
    print(f'Part 1: {result_part1}')

    # Solve Part 2
    result_part2 = part2(input_data)
    print(f'Part 2: {result_part2}')

if __name__ == '__main__':
    main()
