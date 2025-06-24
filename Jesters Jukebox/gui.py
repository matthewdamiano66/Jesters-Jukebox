import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QVBoxLayout
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QColor

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jesters Jukebox")
        self.setGeometry(100, 100, 600, 450) # x, y, width, height

        # Define colors for on/off states
        self.ON_COLOR = "#aaffaa"  # Light green
        self.OFF_COLOR = "#cccccc" # Light gray

        self.button_states = {} # Dictionary to store the state of each button (True for on, False for off)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        grid_layout = QGridLayout()

        self.buttons = []
        rows = 3
        cols = 4
        button_id = 0

        for row in range(rows):
            for col in range(cols):
                button = QPushButton(f"Button {button_id + 1}")
                button.setFixedSize(QSize(100, 100))
                button.clicked.connect(lambda _, id=button_id: self.toggle_button_state(id))
                grid_layout.addWidget(button, row, col)
                self.buttons.append(button)

                # Initialize button state to off and set its initial style
                self.button_states[button_id] = False
                self.set_button_style(button_id, False)

                button_id += 1

        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)

    def set_button_style(self, button_id, is_on):
        """Sets the background color of a button based on its state."""
        button = self.buttons[button_id]
        if is_on:
            button.setStyleSheet(f"background-color: {self.ON_COLOR};")
        else:
            button.setStyleSheet(f"background-color: {self.OFF_COLOR};")

    def toggle_button_state(self, button_id):
        """Toggles the state of a button and updates its appearance."""
        current_state = self.button_states[button_id]
        new_state = not current_state # Flip the state

        self.button_states[button_id] = new_state
        self.set_button_style(button_id, new_state)

        if new_state:
            print(f"Button {button_id + 1} turned ON!")
        else:
            print(f"Button {button_id + 1} turned OFF!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
