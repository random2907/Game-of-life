import time
import copy

def matrix(row: int, col: int) -> list[list[int]]:
    return [[0] * col for _ in range(row)]


reset = '\033[0m'
bg_white = '\033[38;2;255;255;255m'
bg_black = '\033[38;2;0;0;0m'
clear = '\033[2J\033[H'


def sim_start(l: list[list[int]]) -> None:
    while True:
        print(clear, end="")
        for i in l:
            for j in i:
                if j == 0:
                    # print(bg_white + '#'+reset, end=" ")
                    print(bg_white + '█' + reset, end=" ")  # dead

                else:
                    # print(bg_black + '#'+reset, end=" ")
                    print(bg_black + '█' + reset, end=" ")  # alive
            print()
        l=conway_rules(l)
        time.sleep(1)


def count_neighbours(l: list[list[int]], r: int, c: int) -> int:
    directions = [ (-1, 1),
                  (0, 1),
                  (1, 0),
                  (1, 1),
                  (0, -1),
                  (1, -1),
                  (-1, -1),
                  (-1, 0)
                  ]
    count = 0
    for x, y in directions:
        nextx, nexty = r+ x, c+ y
        if 0 <= nextx < len(l) and 0 <= nexty < len(l[0]) and l[nextx][nexty] == 1:
            count+=1
    return count



def conway_rules(l: list[list[int]]) -> list[list[int]]:
    rows, cols = len(l), len(l[0])
    temp = copy.deepcopy(l)

    for r in range(rows):
        for c in range(cols):
            neighbors = count_neighbours(l, r, c)
            if l[r][c] == 1:
                # live cell rules
                if neighbors < 2 or neighbors > 3:
                    temp[r][c] = 0
                else:
                    temp[r][c] = 1
            else:
                # dead cell rule
                if neighbors == 3:
                    temp[r][c] = 1

    return temp

def conway_start() -> None:
    l = matrix(100, 100)
    l[50][52] = 1
    l[51][53] = 1
    l[52][51] = 1
    l[52][52] = 1
    l[52][53] = 1
    sim_start(l)


if __name__ == "__main__":
    conway_start()
