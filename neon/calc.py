from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
 
import sys
 
 
class Window(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python ")
        self.setGeometry(100, 100, 360, 350)
        self.UiComponents()
        self.show()
 
    def UiComponents(self):
        self.label = QLabel(self)
        self.label.setGeometry(5, 5, 350, 70)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont('Arial', 15))
        push1 = QPushButton("1", self)
        push1.setGeometry(5, 150, 80, 40)
        push2 = QPushButton("2", self)
        push2.setGeometry(95, 150, 80, 40)
        push3 = QPushButton("3", self)
        push3.setGeometry(185, 150, 80, 40)
        push4 = QPushButton("4", self)
        push4.setGeometry(5, 200, 80, 40)
        push5 = QPushButton("5", self)
        push5.setGeometry(95, 200, 80, 40)
        push6 = QPushButton("5", self)
        push6.setGeometry(185, 200, 80, 40)
        push7 = QPushButton("7", self)
        push7.setGeometry(5, 250, 80, 40)
        push8 = QPushButton("8", self)
        push8.setGeometry(95, 250, 80, 40)
        push9 = QPushButton("9", self)
        push9.setGeometry(185, 250, 80, 40)
        push0 = QPushButton("0", self)
        push0.setGeometry(5, 300, 80, 40)
        push_equal = QPushButton("=", self)
        push_equal.setGeometry(275, 300, 80, 40)
        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.blue)
        push_equal.setGraphicsEffect(c_effect)
        push_plus = QPushButton("+", self)
        push_plus.setGeometry(275, 250, 80, 40)
        push_minus = QPushButton("-", self)
        push_minus.setGeometry(275, 200, 80, 40)
        push_mul = QPushButton("*", self)
        push_mul.setGeometry(275, 150, 80, 40)
        push_div = QPushButton("/", self)
        push_div.setGeometry(185, 300, 80, 40)
        push_point = QPushButton(".", self)
        push_point.setGeometry(95, 300, 80, 40)
        push_clear = QPushButton("Clear", self)
        push_clear.setGeometry(5, 100, 350, 40)
        push_minus.clicked.connect(self.action_minus)
        push_equal.clicked.connect(self.action_equal)
        push0.clicked.connect(self.action0)
        push1.clicked.connect(self.action1)
        push2.clicked.connect(self.action2)
        push3.clicked.connect(self.action3)
        push4.clicked.connect(self.action4)
        push5.clicked.connect(self.action5)
        push6.clicked.connect(self.action6)
        push7.clicked.connect(self.action7)
        push8.clicked.connect(self.action8)
        push9.clicked.connect(self.action9)
        push_div.clicked.connect(self.action_div)
        push_mul.clicked.connect(self.action_mul)
        push_plus.clicked.connect(self.action_plus)
        push_point.clicked.connect(self.action_point)
        push_clear.clicked.connect(self.action_clear)
 
 
    def action_equal(self):
     
        equation = self.label.text()

        ans = eval(equation)
        self.label.setText(str(ans))

    def action_plus(self):
        text = self.label.text()
        self.label.setText(f"{text} + ")
 
    def action_minus(self):
        text = self.label.text()
        self.label.setText(f"{text} - ")
 
    def action_div(self):
        text = self.label.text()
        self.label.setText(f"{text} / ")
 
    def action_mul(self):
        text = self.label.text()
        self.label.setText(f"{text} * ")
 
    def action_point(self):
        text = self.label.text()
        self.label.setText(f"{text}.")
 
    def action0(self):
        text = self.label.text()
        self.label.setText(f"{text}0")
 
    def action1(self):
        text = self.label.text()
        self.label.setText(f"{text}1")
 
    def action2(self):
        text = self.label.text()
        self.label.setText(f"{text}2")
 
    def action3(self):
        text = self.label.text()
        self.label.setText(f"{text}3")
 
    def action4(self):
        text = self.label.text()
        self.label.setText(f"{text}4")
 
    def action5(self):
        text = self.label.text()
        self.label.setText(f"{text}5")
 
    def action6(self):
        text = self.label.text()
        self.label.setText(f"{text}6")
 
    def action7(self):
        text = self.label.text()
        self.label.setText(f"{text}7")
 
    def action8(self):
        text = self.label.text()
        self.label.setText(f"{text}8")
 
    def action9(self):
        text = self.label.text()
        self.label.setText(f"{text}9")
 
    def action_clear(self):
        self.label.setText("")


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())