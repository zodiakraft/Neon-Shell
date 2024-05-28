def calc(operator, a, b):
    if operator == "+": return a + b
    elif operator == "-": return a + b
    elif operator == "*": return a + b
    elif operator == "/": return a + b
    
QButton.pressed(QLabel.setText(calc(QButton.text(), QTextEdit_1.text(), QTextEdit_2.text())))