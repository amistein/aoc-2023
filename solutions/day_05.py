def part1(data):
    seeds = [int(seed) for seed in data[0].split()[1:]]
    maps = get_maps(data)
                
    return min([get_location(seed, maps) for seed in seeds])


def part2(data):
    maps = get_maps(data)
    all_sources = sum([list(map.keys()) for map in maps], [])
    min_source = min(all_sources)
    max_source = max(all_sources)
    seed_data = [int(seed) for seed in data[0].split()[1:]]
    seeds = []
    for i in range(0, len(seed_data), 2):
        start = max(seed_data[i], min_source)
        end = min(seed_data[i] + seed_data[i + 1], max_source)

        for seed in range(start, end):
            seeds.append(seed)

    return min([get_location(seed, maps) for seed in seeds])

def get_maps(data):
    to_ints = lambda x: [int(n) for n in x]
    seed_soil = {}
    soil_fertilizer = {}
    fertilizer_water = {}
    water_light = {}
    light_temperature = {}
    temperature_humidity = {}
    humidity_location = {}

    maps = [seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location]

    curr_map = -1
    line = 1
    while line < len(data):
        if not data[line]:
            curr_map += 1
            line += 2

        d, s, r = to_ints(data[line].split())
        maps[curr_map][s] = (r, d)
        line += 1

    return maps


def get_location(seed, maps):
    curr = seed
    for curr_map in maps:
        for source, (range, destination) in curr_map.items():
            if curr >= source and curr <= source + range:
                curr = destination + (curr - source)
                break
            
    return curr

def main():
    with open('./inputs/05.txt', 'r') as file:
        input_data = file.read().strip().split('\n')

    # Solve Part 1
    result_part1 = part1(input_data)
    print(f'Part 1: {result_part1}')

    # Solve Part 2
    result_part2 = part2(input_data)
    print(f'Part 2: {result_part2}')

if __name__ == '__main__':
    main()
