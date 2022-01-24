from email import header
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import * 
import time
import random

class Start(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Start, self).__init__(parent)
        self.setWindowTitle("Typing Speed Test!")
        self.setStyleSheet("background-color: #ffffff")

        self.buttonStart = QtWidgets.QPushButton('Start', self)
        self.buttonStart.clicked.connect(self.nextPage)
        self.buttonStart.setStyleSheet("background-color: #4474c2; color: white;")

        headerLabel = QLabel(self)
        headerLabel.setFont(QFont('Times', 40))
        headerLabel.setStyleSheet("color: #4474c2; font-weight: bold")
        headerLabel.setText('Welcome to the Typer Game!')

        firstLabel = QLabel(self)
        firstLabel.setFont(QFont('Times', 20))
        firstLabel.setText("Click to begin, when you click start, the timer begins!")
    
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(40)
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(headerLabel)
        layout.addWidget(firstLabel, alignment=Qt.AlignCenter)
        layout.addWidget(self.buttonStart)

    def nextPage(self):
        self.accept()

class Window(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        startTime = time.perf_counter()

        self.setWindowTitle("Typer Speed Test!")
        self.setStyleSheet("background-color: #FFFFFF")

        '''
        DISPLAY CLOCK TO WORK ON LATER
        clockText = QLabel(self)
        clockText.setFont(QFont('Arial', 20))
        clockText.setText(startTime)
        '''

        headerLabel = QLabel(self)
        headerLabel.setFont(QFont('Times', 40))
        headerLabel.setStyleSheet("color: #4474c2; font-weight: bold")
        headerLabel.setText('Text to type:')

        typeText = self.pickText()
        self.text = QLabel(self)
        self.text.setFont(QFont('Times', 20))
        self.text.setText(typeText)

        self.typingSpace = QtWidgets.QLineEdit(self)
        self.typingSpace.setFixedHeight(80)
    
        self.finalText = QLabel(self)
        self.finalText.setFont(QFont('Times', 20))
        self.finalText.setText("")

        '''
        Restart Button
        self.buttonRestart = QtWidgets.QPushButton('Restart', self)
        self.buttonRestart.clicked.connect(Start.nextPage)
        self.buttonRestart.setStyleSheet("background-color: #4474c2; color: white;")
        '''

        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(headerLabel, alignment=Qt.AlignCenter)
        layout.addWidget(self.text, alignment=Qt.AlignCenter)
        layout.addWidget(self.typingSpace)
        layout.addWidget(self.finalText, alignment=Qt.AlignCenter)
        #layout.addWidget(self.buttonRestart)

        self.typingSpace.textChanged.connect(lambda: self.checkText(typeText,startTime))

    def pickText(self):
        texts = ["abcdefghijklmnopqrstuvwxyz", "I’m not superstitious, but I am a little stitious.", "Identity theft is not a joke, Jim! Millions of families suffer every year."
                ,"We Are! PENN STATE!", "Type this text to test the text to test true.", "We're no strangers to love You know the rules and so do I A full commitment's what I'm thinking of You wouldn't get this from any other guy"]
        pickedText = random.choice(texts)
        return pickedText

    def checkText(self, typeText,startTime):
        if self.typingSpace.text() == typeText:
            endTime = time.perf_counter()
            finalTime = (endTime-startTime)
            finalTime = "{:.2f}".format(finalTime)
            self.finalText.setText("It took " + str(finalTime) + " seconds to type the message!")
        else:
            pass

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    start = Start()
    start.setFixedHeight(500)
    start.setFixedWidth(700)
  
    if start.exec_() == QtWidgets.QDialog.Accepted:
        window = Window()
        window.setFixedHeight(500)
        window.setFixedWidth(700)
        window.show()
        sys.exit(app.exec_())
