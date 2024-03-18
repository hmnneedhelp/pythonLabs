import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QVBoxLayout, QLabel

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Диалоговое окно')
        self.setGeometry(100,100,300,300)
        
        layout = QVBoxLayout()
        label = QLabel('Вы нажали кнопку!')
        layout.addWidget(label)
        
        self.setLayout(layout)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Простой интерфейс')
        button = QPushButton('Нажми меня', self)
        button.setGeometry(100, 100, 100, 50)
        button.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = MyDialog()
        dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
