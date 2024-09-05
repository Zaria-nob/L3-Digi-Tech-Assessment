#print("hello world")

import sys
import random
# * imports all functions from that library
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QInputDialog, QMessageBox, QLabel
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import *

class Whack_a_mole(QWidget):
    #This function has all the variables in it and initializes the code
    def __init__(self):
        super().__init__()
        #Creates variables for the rows, columns, and turns
        self.number_of_rows = 3
        self.number_of_cols = 3
        self.number_of_turns = 0
        self.game_ended = False
        #creates button for mole
    
        self.init_ui()
    
    #Function to set up grid
    def init_ui(self):
        self.setWindowTitle('Whac-A-Mole')

        self.time_limit, ok = QInputDialog.getInt(self, 'Input Dialog', f'Enter the game time in seconds:', min=15, max=60)

        QTimer.singleShot(self.time_limit * 1000, self.end_game)

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.buttons = [[QPushButton('') for _ in range(3)] for _ in range(3)]

        for row in range(self.number_of_rows):
            for col in range(self.number_of_cols):
                button = self.buttons[row][col]
                button.setFixedSize(100,100)
                #button.clicked.connect(lambda ch, row=row, col=col: self.on_click(row, col))
                self.grid.addWidget(button, row, col)
    

    def on_click(self, row, col):
        #print(f'Button at ({row}, {col}) clicked')
        button = self.sender()
        self.number_of_turns += 1
        self.mole_button = self.setGeometry(random.randint())

            

    def end_game(self):
        QMessageBox.information(self, 'Game Over',  f'Game Over! You got a score of {self.number_of_turns}')
        print('Game Over')
        file = open('file.txt', 'w')
        file.close()




class Mole(QWidget):
    def __init__(self):
        #creates button for mole
        self.mole = QPushButton()



    def mole_setup(self):
        #sets position and dimensions of the mole
        self.setGeometry(200, 200, 90, 90)
        
        #makes mole move once clicked
        self.mole_button.clicked.connect(self.on_click)


    def mole_move():
        #sets original position for the mole
        #makes the mole move randomly between the squares in the grid once clicked.
        



# Makes sure it is running the Main code
if __name__ == '__main__':

     # Create an instance of QApplication
    app = QApplication(sys.argv)

    # Create a main application window (QWidget)
    window = Whack_a_mole()
    window.show()
    # Execute the application's event loop
    sys.exit(app.exec_())