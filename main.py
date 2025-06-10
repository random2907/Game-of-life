from PyQt6 import QtCore, QtWidgets, QtGui
import sys
from typing import Tuple, Set
from collections import defaultdict

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



class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.time = 100
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.change)
        self.mylayout = QtWidgets.QVBoxLayout()
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setSpacing(0)
        self.setLayout(self.mylayout)
        self.grid_height = 100
        self.grid_width = 100
        self.live_cells = {
            (50, 52),
            (51, 53),
            (52, 51),
            (52, 52),
            (52, 53),
        }
        
        for i in range(self.grid_height):
            for j in range(self.grid_width):
                cell = QtWidgets.QLabel()
                cell.setFixedSize(10, 10)
                cell.setAutoFillBackground(True)
                self.gridlayout.addWidget(cell, i, j)

        self.slow_button = QtWidgets.QPushButton("<<")
        self.fast_button = QtWidgets.QPushButton(">>")
        self.pause_play_button = QtWidgets.QPushButton()
        self.pause_play_button.setText("")
        self.mylayout.addLayout(self.gridlayout)
        self.buttonlayout = QtWidgets.QGridLayout()
        self.buttonlayout.addWidget(self.slow_button, 1, 1)
        self.buttonlayout.addWidget(self.pause_play_button, 1, 2)
        self.buttonlayout.addWidget(self.fast_button, 1, 3)
        self.mylayout.addLayout(self.buttonlayout)
        self.slow_button.pressed.connect(lambda: self.change_time(-10))
        self.fast_button.pressed.connect(lambda: self.change_time(10))
        self.pause_play_button.pressed.connect(self.player_control)

        self.update_color()
    
    def player_control(self):
        if self.timer.isActive():
            self.pause_play_button.setText('')
            self.timer.stop()
        else:
            self.pause_play_button.setText('')
            self.timer.start(self.time)

    def change_time(self, val: int):
        if self.time - val > 1:
            self.time = self.time - val
            self.timer.setInterval(self.time)
            return self.time
        else:
            return self.time

    def update_color(self):
        for i, j in self.live_cells:
            cell = self.gridlayout.itemAtPosition(i, j)
            if cell:
                label = cell.widget()
                color = QtGui.QColor('black')
                if label:
                    palette = label.palette()
                    palette.setColor(QtGui.QPalette.ColorRole.Window, color)
                    label.setPalette(palette)

    def reset_color(self):
        for i, j in self.live_cells:
            cell = self.gridlayout.itemAtPosition(i, j)
            if cell:
                label = cell.widget()
                if label:
                    palette = label.style()
                    if palette:
                        default_palette = palette.standardPalette()
                        label.setPalette(default_palette)

    def change(self):
        print(f"height is {self.gridlayout.geometry().height()} and width is {self.gridlayout.geometry().width()}")
        self.reset_color()
        self.live_cells = next_Gen(self.live_cells)
        self.update_color()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
