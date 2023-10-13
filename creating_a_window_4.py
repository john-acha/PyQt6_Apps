import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (
	QApplication, 
	QMainWindow,
	QPushButton,
)

# Subclass QMainWindow to customize the application's main window
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("My App")

		button = QPushButton("Press Me!")

		# Set the central widget of the window
		self.setCentralWidget(button)



app = QApplication(sys.argv)


window = MainWindow()
window.show() 

app.exec()