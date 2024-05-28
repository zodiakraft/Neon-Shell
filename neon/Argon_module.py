import contextlib
import serial.tools.list_ports

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import serial
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import Qt
import AModule_design
import PyQt5

def serial_ports():
    if sys.platform.startswith('win'):
        ports = [f'COM{i + 1}' for i in range(256)]
    else:
        raise EnvironmentError('Unsupported platform')

    # for port in ports:
    #     with contextlib.suppress(OSError, serial.SerialException):
    #         s = serial.Serial(port)
    #         s.close()
    #         result.append(port)
    return [str(port) for port in list(serial.tools.list_ports.comports()) if 'Arduino' in str(port)]


class LedApp(QtWidgets.QMainWindow, AModule_design.Ui_MainWindow):
    timer = QTimer()
    
    def __init__(self):
        super().__init__()
        
        self.formated = ''

        self.setupUi(self)
        self.comboBox.addItems(serial_ports())
        self.realport = None
        self.pushButton.clicked.connect(self.connect)
        
        self.timer.setInterval(100) # 100мс
        # Каждые 100мс будет вызываться метод timeStep
        # в котором вы можете перемещать ваших уток
        self.timer.timeout.connect(self.read)

    def connect(self):
        try:
            self.realport = serial.Serial(self.comboBox.currentText())
            self.realport.baudrate = 9600
            self.realport.timeout = 0.2
            print('Подключено')
            # self.cmd = bytes('ati\r\n', 'ascii')  # -1- Добавил '\n'
            # self.realport.write(self.cmd)
            self.timer.start()
        except Exception as e:
            print(e)

    def read(self):
        if self.realport:
            print('Done')
            self.not_formated = str(self.realport.read()).replace('b\'', '').replace('\'', '').replace(r'\r', '').replace(r'\n', '')
            print(self.not_formated)
            self.formated += self.not_formated
            self.textBrowser.setText(self.formated)
            self.timer.start()
        else: print('Error')
            
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = LedApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()