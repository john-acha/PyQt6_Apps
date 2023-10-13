from PyQt6.QtWidgets import QApplication, QWidget
# Only needed for access to command line arguments
import sys



app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()
window.show() # IMPORTANT!!!!! Windows are hidden by default.
# Start the event loop.
app.exec()