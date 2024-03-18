import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Простой интерфейс')

        button = QPushButton('Нажми меня', self)
        button.setGeometry(150, 150, 100, 50)
        button.clicked.connect(self.showMessageBox)

    def showMessageBox(self):
        QMessageBox.information(self, 'Сообщение', 'Вы нажали кнопку!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())