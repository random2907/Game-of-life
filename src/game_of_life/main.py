from PyQt6 import QtCore, QtWidgets, QtGui
from game_of_life.util import next_Gen, Cell, Set
import sys

class GameOfLifeWidget(QtWidgets.QWidget):
    def __init__(self, live_cells, grid_width=100, grid_height=100, cell_size=10):
        super().__init__()
        self.cell_size = cell_size
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.live_cells = live_cells

        self.update_canvas_size()

    def update_canvas_size(self):
        if not self.live_cells:
            return

        max_x = max(x for x, _ in self.live_cells) + 1
        max_y = max(y for _, y in self.live_cells) + 1

        width = max(self.grid_width, max_x)
        height = max(self.grid_height, max_y)

        self.setMinimumSize(width * self.cell_size, height * self.cell_size)

    def set_live_cells(self, live_cells: Set[Cell]):
        self.live_cells = live_cells
        self.update_canvas_size()
        self.update()

    def paintEvent(self, event: QtGui.QPaintEvent): #type: ignore
        painter = QtGui.QPainter(self)
        painter.fillRect(event.rect(), QtCore.Qt.GlobalColor.white)
        painter.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.black))

        rect = event.rect()
        left = rect.left() // self.cell_size
        right = rect.right() // self.cell_size
        top = rect.top() // self.cell_size
        bottom = rect.bottom() // self.cell_size

        for x, y in self.live_cells:
            if left <= x <= right and top <= y <= bottom:
                painter.drawRect(
                    x * self.cell_size,
                    y * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.time = 100


        self.grid_height = 100
        self.grid_width = 100
        self.live_cells = {
            (6+50,1+50),(8+50,1+50),(9+50,1+50),
            (5+50,2+50),(12+50,2+50),
            (4+50,3+50),(5+50,3+50),(9+50,3+50),(12+50,3+50),
            (1+50,4+50),(2+50,4+50),(4+50,4+50),(10+50,4+50),(11+50,4+50),
            (1+50,5+50),(2+50,5+50),(4+50,5+50),(10+50,5+50),(11+50,5+50),
            (4+50,6+50),(5+50,6+50),(9+50,6+50),(12+50,6+50),
            (5+50,7+50),(12+50,7+50),
            (6+50,8+50),(8+50,8+50),(9+50,8+50),
        }
       
        self.mylayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mylayout)

        self.scroll_layout = QtWidgets.QScrollArea()

        self.game_widget = GameOfLifeWidget(
            self.live_cells,
            self.grid_width,
            self.grid_height,
        )

        self.scroll_layout.setWidget(self.game_widget)
        self.mylayout.addWidget(self.scroll_layout)

        # control 
        self.slow_button = QtWidgets.QPushButton("<<")
        self.fast_button = QtWidgets.QPushButton(">>")
        self.pause_play_button = QtWidgets.QPushButton("")
        self.pause_play_button.setFont(QtGui.QFont())

        self.controls = QtWidgets.QHBoxLayout()

        self.controls.addWidget(self.slow_button)
        self.controls.addWidget(self.pause_play_button)
        self.controls.addWidget(self.fast_button)
        self.mylayout.addLayout(self.controls)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.step)

        self.pause_play_button.pressed.connect(self.toggle_timer)
        self.slow_button.pressed.connect(lambda: self.change_time(-10))
        self.fast_button.pressed.connect(lambda: self.change_time(10))

        # self.update_color()
    
    def toggle_timer(self):
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
    
    def step(self):
        self.live_cells = next_Gen(self.live_cells)
        self.game_widget.set_live_cells(self.live_cells)

def main():
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.setWindowTitle("Game of Life")
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())
