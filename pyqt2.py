import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        btn1 = QtGui.QPushButton("Mah jong", self)
        btn1.setStyleSheet("QPushButton:checked { background-color: black }")
        btn1.setCheckable(True)
        btn1.move(30, 10)

        btn2 = QtGui.QPushButton("Dogs", self)
        btn2.setStyleSheet("QPushButton:checked { background-color: black }")
        btn2.setCheckable(True)
        btn2.move(150, 10)

        btn3 = QtGui.QPushButton("Phoenix", self)
        btn3.setStyleSheet("QPushButton:checked { background-color: black }")
        btn3.setCheckable(True)
        btn3.move(270, 10)

        btn4 = QtGui.QPushButton("Dragon", self)
        btn4.setStyleSheet("QPushButton:checked { background-color: black }")
        btn4.setCheckable(True)
        btn4.move(390, 10)

        btn5 = QtGui.QPushButton("Red 2", self)
        btn5.setStyleSheet("QPushButton {background-color: #AA3333;}""QPushButton:checked { background-color: black }")
        btn5.setCheckable(True)
        btn5.move(30, 40)

        btn6 = QtGui.QPushButton("Blue 2", self)
        btn6.setStyleSheet("QPushButton {background-color: #3333AA;}""QPushButton:checked { background-color: black }")
        btn6.setCheckable(True)
        btn6.move(150, 40)

        btn7 = QtGui.QPushButton("Green 2", self)
        btn7.setStyleSheet('QPushButton {background-color: #33AA33;}'"QPushButton:checked { background-color: black }")
        btn7.setCheckable(True)
        btn7.move(270, 40)

        btn8 = QtGui.QPushButton("Black 2", self)
        btn8.setStyleSheet('QPushButton {background-color: #AAAAAA;}'"QPushButton:checked { background-color: black }")
        btn8.setCheckable(True)
        btn8.move(390, 40)

        btn9 = QtGui.QPushButton("Red 3", self)
        btn9.setStyleSheet('QPushButton {background-color: #AA3333;}'"QPushButton:checked { background-color: black }")
        btn9.setCheckable(True)
        btn9.move(30, 70)

        btn10 = QtGui.QPushButton("Blue 3", self)
        btn10.setStyleSheet('QPushButton {background-color: #3333AA;}'"QPushButton:checked { background-color: black }")
        btn10.setCheckable(True)
        btn10.move(150, 70)

        btn11 = QtGui.QPushButton("Green 3", self)
        btn11.setStyleSheet('QPushButton {background-color: #33AA33;}'"QPushButton:checked { background-color: black }")
        btn11.setCheckable(True)
        btn11.move(270, 70)

        btn12 = QtGui.QPushButton("Black 3", self)
        btn12.setStyleSheet('QPushButton {background-color: #AAAAAA;}'"QPushButton:checked { background-color: black }")
        btn12.setCheckable(True)
        btn12.move(390, 70)

        btn13 = QtGui.QPushButton("Red 4", self)
        btn13.setStyleSheet('QPushButton {background-color: #AA3333;}'"QPushButton:checked { background-color: black }")
        btn13.setCheckable(True)
        btn13.move(30, 100)

        btn14 = QtGui.QPushButton("Blue 4", self)
        btn14.setStyleSheet('QPushButton {background-color: #3333AA;}'"QPushButton:checked { background-color: black }")
        btn14.setCheckable(True)
        btn14.move(150, 100)

        btn15 = QtGui.QPushButton("Green 4", self)
        btn15.setStyleSheet('QPushButton {background-color: #33AA33;}'"QPushButton:checked { background-color: black }")
        btn15.setCheckable(True)
        btn15.move(270, 100)

        btn16 = QtGui.QPushButton("Black 4", self)
        btn16.setStyleSheet('QPushButton {background-color: #AAAAAA;}'"QPushButton:checked { background-color: black }")
        btn16.setCheckable(True)
        btn16.move(390, 100)

        btn17 = QtGui.QPushButton("Red 5", self)
        btn17.setStyleSheet('QPushButton {background-color: #AA3333;}'"QPushButton:checked { background-color: black }")
        btn17.setCheckable(True)
        btn17.move(30, 130)

        btn18 = QtGui.QPushButton("Blue 5", self)
        btn18.setStyleSheet('QPushButton {background-color: #3333AA;}'"QPushButton:checked { background-color: black }")
        btn18.setCheckable(True)
        btn18.move(150, 130)

        btn19 = QtGui.QPushButton("Green 5", self)
        btn19.setStyleSheet('QPushButton {background-color: #33AA33;}'"QPushButton:checked { background-color: black }")
        btn19.setCheckable(True)
        btn19.move(270, 130)

        btn20 = QtGui.QPushButton("Black 5", self)
        btn20.setStyleSheet('QPushButton {background-color: #AAAAAA;}'"QPushButton:checked { background-color: black }")
        btn20.setCheckable(True)
        btn20.move(390, 130)

        btn21 = QtGui.QPushButton("Red 6", self)
        btn21.setStyleSheet('QPushButton {background-color: #AA3333;}'"QPushButton:checked { background-color: black }")
        btn21.setCheckable(True)
        btn21.move(30, 160)

        btn22 = QtGui.QPushButton("Blue 6", self)
        btn22.setStyleSheet('QPushButton {background-color: #3333AA;}'"QPushButton:checked { background-color: black }")
        btn22.setCheckable(True)
        btn22.move(150, 160)

        btn23 = QtGui.QPushButton("Green 6", self)
        btn23.setStyleSheet('QPushButton {background-color: #33AA33;}'"QPushButton:checked { background-color: black }")
        btn23.setCheckable(True)
        btn23.move(270, 160)

        btn24 = QtGui.QPushButton("Black 6", self)
        btn24.setStyleSheet('QPushButton {background-color: #AAAAAA;}'"QPushButton:checked { background-color: black }")
        btn24.setCheckable(True)
        btn24.move(390, 160)

        btn25 = QtGui.QPushButton("Red 7", self)
        btn25.setStyleSheet('QPushButton {background-color: #AA3333;}'"QPushButton:checked { background-color: black }")
        btn25.setCheckable(True)
        btn25.move(30, 190)

        btn26 = QtGui.QPushButton("Blue 7", self)
        btn26.setStyleSheet('QPushButton {background-color: #3333AA;}'"QPushButton:checked { background-color: black }")
        btn26.setCheckable(True)
        btn26.move(150, 190)

        btn27 = QtGui.QPushButton("Green 7", self)
        btn27.setStyleSheet('QPushButton {background-color: #33AA33;}'"QPushButton:checked { background-color: black }")
        btn27.setCheckable(True)
        btn27.move(270, 190)

        btn28 = QtGui.QPushButton("Black 7", self)
        btn28.setStyleSheet('QPushButton {background-color: #AAAAAA;}'"QPushButton:checked { background-color: black }")
        btn28.setCheckable(True)
        btn28.move(390, 190)

        btn29 = QtGui.QPushButton("Red 8", self)
        btn29.setStyleSheet('QPushButton {background-color: #AA3333;}'"QPushButton:checked { background-color: black }")
        btn29.setCheckable(True)
        btn29.move(30, 220)

        btn30 = QtGui.QPushButton("Blue 8", self)
        btn30.setStyleSheet('QPushButton {background-color: #3333AA;}'"QPushButton:checked { background-color: black }")
        btn30.setCheckable(True)
        btn30.move(150, 220)

        btn31 = QtGui.QPushButton("Green 8", self)
        btn31.setStyleSheet('QPushButton {background-color: #33AA33;}'"QPushButton:checked { background-color: black }")
        btn31.setCheckable(True)
        btn31.move(270, 220)

        btn32 = QtGui.QPushButton("Black 8", self)
        btn32.setStyleSheet('QPushButton {background-color: #AAAAAA;}'"QPushButton:checked { background-color: black }")
        btn32.setCheckable(True)
        btn32.move(390, 220)

        btn33 = QtGui.QPushButton("Red 9", self)
        btn33.setStyleSheet('QPushButton {background-color: #AA3333;}'"QPushButton:checked { background-color: black }")
        btn33.setCheckable(True)
        btn33.move(30, 250)

        btn34 = QtGui.QPushButton("Blue 9", self)
        btn34.setStyleSheet('QPushButton {background-color: #3333AA;}'"QPushButton:checked { background-color: black }")
        btn34.setCheckable(True)
        btn34.move(150, 250)

        btn35 = QtGui.QPushButton("Green 9", self)
        btn35.setStyleSheet('QPushButton {background-color: #33AA33;}'"QPushButton:checked { background-color: black }")
        btn35.setCheckable(True)
        btn35.move(270, 250)

        btn36 = QtGui.QPushButton("Black 9", self)
        btn36.setStyleSheet('QPushButton {background-color: #AAAAAA;}'"QPushButton:checked { background-color: black }")
        btn36.setCheckable(True)
        btn36.move(390, 250)

        btn37 = QtGui.QPushButton("Red 10", self)
        btn37.setStyleSheet('QPushButton {background-color: #AA3333;}'"QPushButton:checked { background-color: black }")
        btn37.setCheckable(True)
        btn37.move(30, 280)

        btn38 = QtGui.QPushButton("Blue 10", self)
        btn38.setStyleSheet('QPushButton {background-color: #3333AA;}'"QPushButton:checked { background-color: black }")
        btn38.setCheckable(True)
        btn38.move(150, 280)

        btn39 = QtGui.QPushButton("Green 10", self)
        btn39.setStyleSheet('QPushButton {background-color: #33AA33;}'"QPushButton:checked { background-color: black }")
        btn39.setCheckable(True)
        btn39.move(270, 280)

        btn40 = QtGui.QPushButton("Black 10", self)
        btn40.setStyleSheet('QPushButton {background-color: #AAAAAA;}'"QPushButton:checked { background-color: black }")
        btn40.setCheckable(True)
        btn40.move(390, 280)

        btn41 = QtGui.QPushButton("Red J", self)
        btn41.setStyleSheet('QPushButton {background-color: #AA3333;}'"QPushButton:checked { background-color: black }")
        btn41.setCheckable(True)
        btn41.move(30, 310)

        btn42 = QtGui.QPushButton("Blue J", self)
        btn42.setStyleSheet('QPushButton {background-color: #3333AA;}'"QPushButton:checked { background-color: black }")
        btn42.setCheckable(True)
        btn42.move(150, 310)

        btn43 = QtGui.QPushButton("Green J", self)
        btn43.setStyleSheet('QPushButton {background-color: #33AA33;}'"QPushButton:checked { background-color: black }")
        btn43.setCheckable(True)
        btn43.move(270, 310)

        btn44 = QtGui.QPushButton("Black J", self)
        btn44.setStyleSheet('QPushButton {background-color: #AAAAAA;}'"QPushButton:checked { background-color: black }")
        btn44.setCheckable(True)
        btn44.move(390, 310)

        btn45 = QtGui.QPushButton("Red Q", self)
        btn45.setStyleSheet('QPushButton {background-color: #AA3333;}'"QPushButton:checked { background-color: black }")
        btn45.setCheckable(True)
        btn45.move(30, 340)

        btn46 = QtGui.QPushButton("Blue Q", self)
        btn46.setStyleSheet('QPushButton {background-color: #3333AA;}'"QPushButton:checked { background-color: black }")
        btn46.setCheckable(True)
        btn46.move(150, 340)

        btn47 = QtGui.QPushButton("Green Q", self)
        btn47.setStyleSheet('QPushButton {background-color: #33AA33;}'"QPushButton:checked { background-color: black }")
        btn47.setCheckable(True)
        btn47.move(270, 340)

        btn48 = QtGui.QPushButton("Black Q", self)
        btn48.setStyleSheet('QPushButton {background-color: #AAAAAA;}'"QPushButton:checked { background-color: black }")
        btn48.setCheckable(True)
        btn48.move(390, 340)

        btn49 = QtGui.QPushButton("Red K", self)
        btn49.setStyleSheet('QPushButton {background-color: #AA3333;}'"QPushButton:checked { background-color: black }")
        btn49.setCheckable(True)
        btn49.move(30, 370)

        btn50 = QtGui.QPushButton("Blue K", self)
        btn50.setStyleSheet('QPushButton {background-color: #3333AA;}'"QPushButton:checked { background-color: black }")
        btn50.setCheckable(True)
        btn50.move(150, 370)

        btn51 = QtGui.QPushButton("Green K", self)
        btn51.setStyleSheet('QPushButton {background-color: #33AA33;}'"QPushButton:checked { background-color: black }")
        btn51.setCheckable(True)
        btn51.move(270, 370)

        btn52 = QtGui.QPushButton("Black K", self)
        btn52.setStyleSheet('QPushButton {background-color: #AAAAAA;}'"QPushButton:checked { background-color: black }")
        btn52.setCheckable(True)
        btn52.move(390, 370)

        btn53 = QtGui.QPushButton("Red A", self)
        btn53.setStyleSheet('QPushButton {background-color: #AA3333;}'"QPushButton:checked { background-color: black }")
        btn53.setCheckable(True)
        btn53.move(30, 400)

        btn54 = QtGui.QPushButton("Blue A", self)
        btn54.setStyleSheet('QPushButton {background-color: #3333AA;}'"QPushButton:checked { background-color: black }")
        btn54.setCheckable(True)
        btn54.move(150, 400)

        btn55 = QtGui.QPushButton("Green A", self)
        btn55.setStyleSheet('QPushButton {background-color: #33AA33;}'"QPushButton:checked { background-color: black }")
        btn55.setCheckable(True)
        btn55.move(270, 400)

        btn56 = QtGui.QPushButton("Black A", self)
        btn56.setStyleSheet('QPushButton {background-color: #AAAAAA;}'"QPushButton:checked { background-color: black }")
        btn56.setCheckable(True)
        btn56.move(390, 400)
      
        btn1.clicked.connect(self.buttonClicked)            
        btn2.clicked.connect(self.buttonClicked)
        btn3.clicked.connect(self.buttonClicked)            
        btn4.clicked.connect(self.buttonClicked)
        btn5.clicked.connect(self.buttonClicked)            
        btn6.clicked.connect(self.buttonClicked)
        btn7.clicked.connect(self.buttonClicked)            
        btn8.clicked.connect(self.buttonClicked)

        
        self.statusBar()
        
        self.setGeometry(0, 0, 520, 450)
        self.setWindowTitle('Tichu Assistant')
        self.show()
        
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 
