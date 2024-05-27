import sys
from PyQt5 import QtWidgets, uic

class CylinderCalculator(QtWidgets.QMainWindow):
    def __init__(self):
        super(CylinderCalculator, self).__init__()
        uic.loadUi('cylinder.ui', self)
        
        # Привязываем кнопку к методу расчета
        self.calculateButton.clicked.connect(self.calculate)
    
    def calculate(self):
        try:
            # Получаем значения, введенные пользователем
            height = float(self.heightInput.text())
            diameter = float(self.diameterInput.text())
            density = float(self.densityInput.text())
            
            # Вычисляем объем цилиндра
            radius = diameter / 2
            volume = 3.14159 * (radius ** 2) * height  # πr²h
            
            # Вычисляем массу цилиндра
            mass = volume * density
            
            # Отображаем результаты
            self.volumeOutput.setText(f'Объем: {volume:.2f} см³')
            self.massOutput.setText(f'Масса: {mass:.2f} г')
        
        except ValueError:
            # Если произошла ошибка преобразования, сообщаем пользователю
            self.volumeOutput.setText('Ошибка ввода!')
            self.massOutput.setText('Пожалуйста, введите числа.')
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CylinderCalculator()
    window.show()
    sys.exit(app.exec_())
