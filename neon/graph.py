# importing various libraries
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random

class Window(QDialog):
	
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)
		self.figure = plt.figure()
		self.canvas = FigureCanvas(self.figure)
		self.toolbar = NavigationToolbar(self.canvas, self)
		self.button = QPushButton('Plot')
		self.button.clicked.connect(self.plot)
		layout = QVBoxLayout()
		layout.addWidget(self.toolbar)
		layout.addWidget(self.canvas)
		layout.addWidget(self.button)
		self.setLayout(layout)

	def plot(self):
		
		data = [random.random() for _ in range(10)]
		self.figure.clear()
		ax = self.figure.add_subplot(111)
		ax.plot(data, '*-')
		self.canvas.draw()

	self.figure.clear()
	ax = self.figure.add_subplot(111)
	ax.plot(data, '*-')
	self.canvas.draw()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	main = Window()
	main.show()
	sys.exit(app.exec_())
