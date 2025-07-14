from collections import defaultdict
from typing import Tuple, Set

Cell = Tuple[int, int]

def next_Gen(live_cells: Set[Cell]) -> Set[Cell]:
    neighbour_counts = defaultdict(int)

    for x, y in live_cells:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:
                    neighbour_counts[(x+dx, y+dy)] += 1
    new_live_cells = set()

    for cell, count in neighbour_counts.items():
        if count == 3 or (count == 2 and cell in live_cells):
            new_live_cells.add(cell)

    return new_live_cells

def simple_rle_decode(rle: str):
    lines = rle.strip().splitlines()
    pattern_lines = [line for line in lines if not line.startswith('#') and not line.startswith('x')]
    pattern = ''.join(pattern_lines).replace('\n', '').replace('!', '')

    x = y = 0
    num = ''
    live_cells = set()

    for char in pattern:
        if char.isdigit():
            num += char
        elif char in 'bo':
            count = int(num) if num else 1
            if char == 'o':
                for i in range(count):
                    live_cells.add((x + i, y))
            x += count
            num = ''
        elif char == '$':
            count = int(num) if num else 1
            y += count
            x = 0
            num = ''
    return live_cells

