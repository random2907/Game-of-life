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

