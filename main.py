from PyQt6 import QtCore, QtWidgets, QtGui
import sys
import copy

def matrix(row: int, col: int) -> list[list[int]]:
    return [[0] * col for _ in range(row)]

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



class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.mylayout = QtWidgets.QGridLayout()
        self.mylayout.setSpacing(0)
        self.setLayout(self.mylayout)
        self.grid_height = 100
        self.grid_width = 100
        self.grid = matrix(self.grid_height, self.grid_width)
        self.grid[50][52] = 1
        self.grid[51][53] = 1
        self.grid[52][51] = 1
        self.grid[52][52] = 1
        self.grid[52][53] = 1
        
        for i in range(self.grid_height):
            for j in range(self.grid_width):
                cell = QtWidgets.QLabel()
                cell.setFixedSize(10, 10)
                cell.setAutoFillBackground(True)
                self.mylayout.addWidget(cell, i, j)
        button = QtWidgets.QPushButton("Push me")
        self.mylayout.addWidget(button)
        self.update_color()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.change)
        self.timer.start(17) 
        button.pressed.connect(lambda: self.timer.stop() if self.timer.isActive() else self.timer.start(17))

    def update_color(self):
        for i in range(self.grid_height):
                for j in range(self.grid_width):
                    cell = self.mylayout.itemAtPosition(i, j)
                    if cell:
                        label = cell.widget()
                        color = QtGui.QColor('black') if self.grid[i][j] == 1 else QtGui.QColor('white')
                        if label:
                            pallete = label.palette()
                            pallete.setColor(QtGui.QPalette.ColorRole.Window, color)
                            label.setPalette(pallete)

    def change(self):
        self.grid = conway_rules(self.grid)
        self.update_color()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
