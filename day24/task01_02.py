# https://www.reddit.com/r/adventofcode/comments/7lte5z/2017_day_24_solutions/droveqk

from collections import defaultdict


def gen_bridges(bridge, components):
    bridge = bridge or [(0, 0)]
    cur = bridge[-1][1]
    for b in components[cur]:
        if not ((cur, b) in bridge or (b, cur) in bridge):
            new = bridge + [(cur, b)]
            yield new
            yield from gen_bridges(new, components)


def parse_components(_input):
    components = defaultdict(set)
    with open(_input) as f:
        for l in [line.strip() for line in f]:
            a, b = [int(x) for x in l.split('/')]
            components[a].add(b)
            components[b].add(a)
        return components


def solve(_input):
    components = parse_components(_input)
    mx = []
    for bridge in gen_bridges(None, components):
        mx.append((len(bridge), sum(a + b for a, b in bridge)))
    return mx


solution = solve("input.txt")
part1 = sorted(solution, key=lambda x: x[1])[-1][1]
part2 = sorted(solution)[-1][1]

print(part1)
print(part2)
