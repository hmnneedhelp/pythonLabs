import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtWidgets, uic

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super(MplCanvas, self).__init__(self.fig)

class QuadraticPlotter(QtWidgets.QMainWindow):
    def __init__(self):
        super(QuadraticPlotter, self).__init__()
        uic.loadUi('quadratic_plot.ui', self)
        
        # Добавляем график на форму
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.plotLayout = QtWidgets.QVBoxLayout(self.plotWidget)
        self.plotLayout.addWidget(self.canvas)
        
        # Привязываем кнопку к методу расчета
        self.calculateButton.clicked.connect(self.plot_quadratic_function)
    
    def plot_quadratic_function(self):
        try:
            # Получаем значения, введенные пользователем
            x_min = float(self.xMinInput.text())
            x_max = float(self.xMaxInput.text())
            x_shift = float(self.xShiftInput.text())
            y_shift = float(self.yShiftInput.text())
            
            # Генерируем значения X
            x = np.linspace(x_min, x_max, 400)
            # Вычисляем значения Y для квадратичной функции
            y = (x - x_shift) ** 2 + y_shift
            
            # Очищаем предыдущий график и рисуем новый
            self.canvas.ax.clear()
            self.canvas.ax.plot(x, y, label='y = (x - a)² + b')
            self.canvas.ax.legend()
            self.canvas.ax.grid(True)
            self.canvas.draw()
        
        except ValueError:
            # Если произошла ошибка преобразования, сообщаем пользователю
            QtWidgets.QMessageBox.warning(self, 'Ошибка ввода', 'Пожалуйста, введите корректные числа.')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QuadraticPlotter()
    window.show()
    sys.exit(app.exec_())
