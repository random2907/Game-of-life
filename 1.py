import time


def matrix(row: int, col: int):
    return [[0] * col for _ in range(row)]


reset = '\033[0m'
bg_white = '\033[38;2;255;255;255m'
bg_black = '\033[38;2;0;0;0m'
clear = '\033[2J\033[H'


def sim_start(l: list[list[int]]):
    while True:
        print(clear, end="")
        for i in l:
            for j in i:
                if j == 0:
                    print(bg_white + '#'+reset, end=" ")
                else:
                    print(bg_black + '#'+reset, end=" ")
            print()
        time.sleep(1)


def calculate_neighbours(l: list[list[int]]):
    full_neighbours = []
    for row_idx, row in enumerate(l):
        for col_idx, value in enumerate(row):
            if value == 1:
                neighbours = {}
                neighbours["alive"] = True
                neighbours["row"] = row_idx
                neighbours["col"] = col_idx
                neighbours["neighbour"] = [
                    [row_idx, col_idx + 1],
                    [row_idx, col_idx - 1],
                    [row_idx + 1, col_idx],
                    [row_idx - 1, col_idx],
                    [row_idx + 1, col_idx - 1],
                    [row_idx - 1, col_idx + 1],
                    [row_idx + 1, col_idx + 1],
                    [row_idx - 1, col_idx - 1],
                ]
                full_neighbours.append(neighbours)
    return full_neighbours


def conway_rules(l: list[list[int]]):
    #    Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    #    Any live cell with two or three live neighbours lives on to the next generation.
    #    Any live cell with more than three live neighbours dies, as if by overpopulation.
    #    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

    neighbours = calculate_neighbours(l)
    for cell in neighbours:
        print("before: ",cell)
        count = 0
        for neighbour in cell["neighbour"]:
            if l[neighbour[0]][neighbour[1]] == 1:
                count+=1

        if cell["alive"]:
            if (count < 2 or count > 3):
                print("death")
                l[cell["row"]][cell["col"]] = 0
            else: 
                l[cell["row"]][cell["col"]] = 1
            for dead_neighbour in 
                if count==3:
                    print("birth")
                    l[cell["row"]][cell["col"]] = 1

    neighbours = calculate_neighbours(l)
    for cell in neighbours:
        print("after: ",cell)


def conway_start():
    l = matrix(100, 100)
    l[50][52] = 1
    l[51][53] = 1
    l[52][51] = 1
    l[52][52] = 1
    l[52][53] = 1
    conway_rules(l)

    # sim_start(l)


if __name__ == "__main__":
    conway_start()
