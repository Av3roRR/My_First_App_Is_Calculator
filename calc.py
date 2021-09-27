# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()

        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        font.setWeight(50)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(1, 1, 600, 100)
        self.label.setStyleSheet("background-color: brown")
        self.label.setFont(font)
        self.label.setText('0')

        self.clear = QtWidgets.QPushButton(self)
        self.clear.setGeometry(232, 291, 75, 75)
        self.clear.setObjectName('clear')

        self.split = QtWidgets.QPushButton(self)
        self.split.setGeometry(232, 367, 75, 75)
        self.split.setObjectName('split')

        self.multiply = QtWidgets.QPushButton(self)
        self.multiply.setGeometry(232, 443, 75, 75)
        self.multiply.setObjectName('multiply')

        self.equal = QtWidgets.QPushButton(self)
        self.equal.setGeometry(232, 520, 75, 75)
        self.equal.setObjectName('equal')

        self.minus = QtWidgets.QPushButton(self)
        self.minus.setGeometry(155, 520, 75, 75)
        self.minus.setObjectName('minus')

        self.plus = QtWidgets.QPushButton(self)
        self.plus.setGeometry(1, 520, 75, 75)
        self.plus.setObjectName('plus')

        self.zero = QtWidgets.QPushButton(self)
        self.zero.setGeometry(78, 520, 75, 75)
        self.zero.setObjectName('zero')

        self.one = QtWidgets.QPushButton(self)
        self.one.setGeometry(1, 443, 75, 75)
        self.one.setObjectName('one')

        self.two = QtWidgets.QPushButton(self)
        self.two.setGeometry(78, 443, 75, 75)
        self.two.setObjectName('two')

        self.three = QtWidgets.QPushButton(self)
        self.three.setGeometry(155, 443, 75, 75)
        self.three.setObjectName('three')

        self.four = QtWidgets.QPushButton(self)
        self.four.setGeometry(1, 367, 75, 75)
        self.four.setObjectName('four')

        self.five = QtWidgets.QPushButton(self)
        self.five.setGeometry(78, 367, 75, 75)
        self.five.setObjectName('five')

        self.six = QtWidgets.QPushButton(self)
        self.six.setGeometry(155, 367, 75, 75)
        self.six.setObjectName('six')

        self.seven = QtWidgets.QPushButton(self)
        self.seven.setGeometry(1, 291, 75, 75)
        self.seven.setObjectName('seven')

        self.eight = QtWidgets.QPushButton(self)
        self.eight.setGeometry(78, 291, 75, 75)
        self.eight.setObjectName('eight')

        self.nine = QtWidgets.QPushButton(self)
        self.nine.setGeometry(155, 291, 75, 75)
        self.nine.setObjectName('nine')

        self.initUi()

    def initUi(self):
        self.setGeometry(QtCore.QRect(100, 100, 600, 600))

        self.add_func()
        self.setWindowIcon(QIcon('cal.png'))
        self.show()

    def add_func(self):
        self.zero.clicked.connect(lambda: self.write_number('0'))
        self.one.clicked.connect(lambda: self.write_number('1'))
        self.two.clicked.connect(lambda: self.write_number('2'))
        self.three.clicked.connect(lambda: self.write_number('3'))
        self.four.clicked.connect(lambda: self.write_number('4'))
        self.five.clicked.connect(lambda: self.write_number('5'))
        self.six.clicked.connect(lambda: self.write_number('6'))
        self.seven.clicked.connect(lambda: self.write_number('7'))
        self.eight.clicked.connect(lambda: self.write_number('8'))
        self.nine.clicked.connect(lambda: self.write_number('9'))
        self.split.clicked.connect(lambda: self.write_number('/'))
        self.multiply.clicked.connect(lambda: self.write_number('*'))
        self.plus.clicked.connect(lambda: self.write_number('+'))
        self.minus.clicked.connect(lambda: self.write_number('-'))
        self.clear.clicked.connect(lambda: self.c())
        self.equal.clicked.connect(lambda: self.results())

    def write_number(self, number):
        if self.label.text() == '0':
            self.label.setText(number)
        else:
            self.label.setText(self.label.text() + number)

    def results(self):
        res = eval(self.label.text())
        if int(res) - float(res) == 0:
            self.label.setText(str(int(res)))
        else:
            self.label.setText(str(res))


    def c(self):
        self.label.setText('0')


qss = '''
    #equal {
        border: none;
        margin: 0px;
        padding: 0px;
        border-image: url(equal.png);        
    }
    #equal:pressed {
        border-image: url(equal_used.png);
    }
    #minus {
        border: none;
        margin: 0px;
        padding: 0px;
        border-image: url(minus.png);        
    }
    #minus:pressed {
        border-image: url(minus_used.png);
    }
    #plus {
        border: none;
        margin: 0px;
        padding: 0px;
        border-image: url(plus.png);        
    }
    #plus:pressed {
        border-image: url(plus_used.png);
    }
    #split {
        border: none;
        margin: 0px;
        padding: 0px;
        border-image: url(split.png);        
    }
    #split:pressed {
        border-image: url(split_used.png);
    }
    #multiply {
        border: none;
        margin: 0px;
        padding: 0px;
        border-image: url(multiplication.png);        
    }
    #multiply:pressed {
        border-image: url(multiplication_used.png);
    }
    #clear {
        border: none;
        margin: 0px;
        padding: 0px;
        border-image: url(clear.png);        
    }
    #clear:pressed {
        border-image: url(clear_used.png);
    }
    #zero {
        border: none;
        margin: 0px;
        padding: 0px;
        border-image: url(number0.png);        
    }
    #zero:pressed {
        border-image: url(number0_used.png);
    }
    #one {
        border: none;
        margin: 0px;
        padding: 0px;
        border-image: url(number1.png);        
    }
    #one:pressed {
        border-image: url(number1_used.png);
    }
    #two {
        border: none;
        margin: 0px;
        padding: 0px;
        border-image: url(number2.png);        
    }
    #two:pressed {
        border-image: url(number2_used.png);
    }
    #three {
        border: none;
        margin: 0px;
        padding: 0px;
        border-image: url(number3.png);        
    }
    #three:pressed {
        border-image: url(number3_used.png);
    }
    #four {
        border: none;
        margin: 0px;
        padding: 0px;
        border-image: url(number4.png);        
    }
    #four:pressed {
        border-image: url(number4_used.png);
    }
    #five {
        border: none;
        margin: 0px;
        padding: 0px;
        border-image: url(number5.png);        
    }
    #five:pressed {
        border-image: url(number5_used.png);
    }
    #six {
        border: none;
        margin: 0px;
        padding: 0px;
        border-image: url(number6.png);        
    }
    #six:pressed {
        border-image: url(number6_used.png);
    }
    #seven {
        border: none;
        margin: 0px;
        padding: 0px;
        border-image: url(number7.png);        
    }
    #seven:pressed {
        border-image: url(number7_used.png);
    }
    #eight {
        border: none;
        margin: 0px;
        padding: 0px;
        border-image: url(number8.png);        
    }
    #eight:pressed {
        border-image: url(number8_used.png);
    }
    #nine {
        border: none;
        margin: 0px;
        padding: 0px;
        border-image: url(number9.png);        
    }
    #nine:pressed {
        border-image: url(number9_used.png);
    }
    '''


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qss)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())