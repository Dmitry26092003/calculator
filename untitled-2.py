import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QSpinBox
from SisVibor import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ev = []
        self.pushButton.clicked.connect(self.run)
        
    def run(self):
        open('sistem.txt', 'w').write(str(self.spinBox.value()))
        sys.exit()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec())
