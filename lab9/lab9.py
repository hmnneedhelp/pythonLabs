import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5.uic import loadUi

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi('main.ui', self) 

        self.openFileButton.clicked.connect(self.open_file)
        self.closeFileButton.clicked.connect(self.close_file)

        self.current_file = None

    def open_explorer(self):
        os.startfile(os.getcwd())

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Выберите текстовый файл', '', 'Текстовые файлы (*.txt)')
        if file_path:
            with open(file_path, 'r') as file:
                self.textBrowser.setText(file.read())
                self.current_file = file
                self.closeFileButton.setEnabled(True)

    def close_file(self):
        if self.current_file:
            self.current_file.close()
            self.current_file = None
            self.textBrowser.clear()
            self.closeFileButton.setEnabled(False)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
