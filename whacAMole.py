#print("hello world")

import sys
import random
# * imports all functions from that library
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QInputDialog, QMessageBox, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import *

class Whack_a_mole(QWidget):
    #This function has all the variables in it and initializes the code
    def __init__(self):
        super().__init__()
        #Creates variables for the rows, columns, mole position, and turns
        self.number_of_rows = 3
        self.number_of_cols = 3
        self.score = 0
        self.game_ended = False
        #initializes mole_position
        self.mole_position = (-1,-1) 
    
        self.init_ui()
    
    #Function to set up grid
    def init_ui(self):
        #This creates the name and dimensions of the window
        self.setWindowTitle('Whack-A-Mole')
        self.setGeometry(300,200,350,400)

        self.layout = QVBoxLayout()

        #this creates the pop up box for the time limit
        self.score_label = QLabel(f'Score: {self.score}', self)
        self.layout.addWidget(self.score_label)

        #This includes the text and min and max
        self.time_limit, ok = QInputDialog.getInt(self, 'Input Dialog', f'Enter the game time in seconds:', min=15, max=60)
        if not ok:
            #closes the program if input was cancelled
            self.close()
    
        #this starts the timer and times it by 1000 to convert it to seconds.
        QTimer.singleShot(self.time_limit * 1000, self.end_game)

        #creates the grid for the main game
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        #this creates a set to store the buttons
        self.buttons = {}

        #This creates the buttons for the grid
        for row in range(self.number_of_rows):
            for col in range(self.number_of_cols):
                button = QPushButton('', self)
                button.setFixedSize(100,100)
                button.clicked.connect(lambda ch, r=row, c=col: self.on_click(r, c))
                self.grid.addWidget(button, row, col)
                self.buttons[(row, col)] = button

        self.layout.addLayout(self.grid)
        self.setLayout(self.layout)

        #move the mole initially
        self.mole_move

        #create a timer to move the mole every second
        self.mole_timer = QTimer(self)
        self.mole_timer.timeout.connect(self.mole_move)
        self.mole_timer.start(1000)



    def mole_move(self):
        #sets original position for the mole
        if self.mole_position != (-1,-1):
            self.buttons[self.mole_position].setText('')
        
        #makes the mole move randomly between the squares in the grid once clicked.
        self.mole_position = (random.randint(0, 2), random.randint(0, 2))
        self.buttons[self.mole_position].setText('Mole!')
        


    #finds out if the clicked position is where the mole is and then adds to the score if it is correct
    def on_click(self, row, col):
        if (row, col) == self.mole_position:
            self.score += 1
            #updates score label after you score
            self.score_label.setText(f'Score: {self.score}')
            self.buttons[self.mole_position].setText('')
        else:
            #Prints in the terminal when the player misses a mole
            print('you missed the mole')



    def end_game(self):
        #stops moving the mole
        self.mole_timer.stop()
        #shows the final score in a pop up window
        QMessageBox.information(self, 'Game Over',  f'Game Over! You got a score of {self.score}')
        print('Game Over')
        file = open('file.txt', 'w')
        #closes file
        file.close()
        


# Makes sure it is running the Main code
if __name__ == '__main__':

     # Create an instance of QApplication
    app = QApplication(sys.argv)

    # Create a main application window (QWidget)
    window = Whack_a_mole()
    window.show()
    # Execute the application's event loop
    sys.exit(app.exec_())