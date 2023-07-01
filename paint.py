import figure_maker
import pnt_parametres
import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, \
    QGraphicsScene, QGridLayout, QPushButton, QMainWindow, QWidget, QAction, \
    QToolBar, QSlider, QInputDialog
from PyQt5.QtCore import QPointF, Qt, QSize
from PyQt5.QtGui import QPen, QIcon, QColor
import saver
import opener


color_brush = (255, 127, 255)
color_pen = (255, 127, 255)
width = 1
figure = "plus"
wind = None


class Paint(QGraphicsView):
    def __init__(self):
        QGraphicsView.__init__(self)
        self.setFixedWidth(600)
        self.setFixedHeight(450)
        self.setSceneRect(0, 0, 500, 500)
        self.scene = QGraphicsScene()
        self.isClear = False
        self.isBack = False
        self.first_click = (0, 0)
        self.sec_clicked = True
        self.third_clicked = False
        self.second_click = (0, 0)
        self.gradient = False
        self.fx = 0
        self.fy = 0
        self.sx = 0
        self.sy = 0
        self.tx = 0
        self.ty = 0

    def tools(self):
        """Добавляет соответствующие примитивы на сцену"""
        global figure,  color_brush
        pen = QPen(QColor(color_pen[0], color_pen[1], color_pen[2]), width)
        if figure == 'rect':
            rect = figure_maker.create_rect_or_ell(self.fx, self.fy, self.sx,
                                                   self.sy, color_pen,
                                                   color_brush, width,
                                                   self.gradient, figure)
            self.scene.addItem(self.scene.addRect(*rect))
        elif figure == 'line':
            self.scene.addItem(
                self.scene.addLine(self.fx, self.fy, self.sx,
                                   self.sy, pen))
            saves = saver.save_line(self.fx, self.fy, self.sx, self.sy, width,
                                    color_pen)
            saver.file += saves
        elif figure == 'ellipse':
            ell = figure_maker.create_rect_or_ell(self.fx, self.fy, self.sx,
                                                  self.sy, color_pen,
                                                  color_brush, width,
                                                  self.gradient, figure)
            self.scene.addItem(self.scene.addEllipse(*ell))
        elif figure == 'triangle':
            triangle = figure_maker.create_triangle(self.fx, self.fy, self.sx,
                                                    self.sy, self.tx, self.ty,
                                                    color_pen, color_brush,
                                                    width, self.gradient)
            self.scene.addItem(self.scene.addPolygon(*triangle))
        elif figure == 'heart':
            heart = figure_maker.create_heart(self.fx, self.fy, color_pen,
                                              color_brush, width,
                                              self.gradient)
            self.scene.addPath(*heart[0])
            self.scene.addPath(*heart[1])
        elif figure == 'star':
            star = figure_maker.create_star(self.fx, self.fy, color_pen,
                                            color_brush, width, self.gradient)
            self.scene.addItem(self.scene.addPolygon(*star))
        elif figure == 'plus':
            plus = figure_maker.create_plus(self.fx, self.fy, color_pen,
                                            color_brush, width, self.gradient)
            self.scene.addItem(self.scene.addPolygon(*plus))
        self.setScene(self.scene)

    def mousePressEvent(self, event):
        global figure
        if figure == 'heart' or figure == 'star' or figure == 'plus':
            self.first_click = QPointF(self.mapToScene(event.pos()))
            self.fx = self.first_click.x()
            self.fy = self.first_click.y()
            self.tools()
            return
        if self.sec_clicked:
            self.first_click = QPointF(self.mapToScene(event.pos()))
            self.sec_clicked = False
            self.third_clicked = False
        else:
            if figure == 'triangle' and self.third_clicked:
                third_click = QPointF(self.mapToScene(event.pos()))
                self.fx = self.first_click.x()
                self.fy = self.first_click.y()
                self.sx = self.second_click.x()
                self.sy = self.second_click.y()
                self.tx = third_click.x()
                self.ty = third_click.y()
                self.tools()
                self.sec_clicked = True
            self.second_click = QPointF(self.mapToScene(event.pos()))
            self.third_clicked = True
            if figure != 'triangle':
                self.fx = self.first_click.x()
                self.fy = self.first_click.y()
                self.sx = self.second_click.x()
                self.sy = self.second_click.y()
                self.tools()
                self.sec_clicked = True


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.make_window()

    def make_window(self):
        global color_brush
        self.main_widget = PaintWidget()
        self.setCentralWidget(self.main_widget)
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('Векторная графика на минималках')
        self.statusBar()

        menu = self.menuBar()
        saveMenu = menu.addMenu("Файл")
        save = QAction("Сохранить", self)
        save.triggered.connect(self.is_save)
        saveMenu.addAction(save)
        open = QAction("Открыть", self)
        open.triggered.connect(self.is_open)
        saveMenu.addAction(open)

        line = QAction(QIcon('line.png'), "Линия", self)
        line.triggered.connect(self.choose_figure)
        rect = QAction(QIcon('rectangle.png'), "Прямоугольник", self)
        rect.triggered.connect(self.choose_figure)
        circle = QAction(QIcon('ellipse.png'), "Эллипс", self)
        circle.triggered.connect(self.choose_figure)
        triangle = QAction(QIcon('triangle.png'), "Треугольник", self)
        triangle.triggered.connect(self.choose_figure)
        heart = QAction(QIcon('heart.png'), "Сердце", self)
        heart.triggered.connect(self.choose_figure)
        star = QAction(QIcon('star.png'), "Звезда", self)
        star.triggered.connect(self.choose_figure)
        plus = QAction(QIcon('plus.png'), "Плюс", self)
        plus.triggered.connect(self.choose_figure)

        red = QAction(QIcon('red.png'), "Красный", self)
        red.triggered.connect(self.choose_color_brush)
        green = QAction(QIcon('green.png'), "Зеленый", self)
        green.triggered.connect(self.choose_color_brush)
        blue = QAction(QIcon('blue.png'), "Синий", self)
        blue.triggered.connect(self.choose_color_brush)
        white = QAction(QIcon('white.png'), "Белый", self)
        white.triggered.connect(self.choose_color_brush)
        black = QAction(QIcon('black.png'), "Черный", self)
        black.triggered.connect(self.choose_color_brush)
        yellow = QAction(QIcon('yellow.png'), "Желтый", self)
        yellow.triggered.connect(self.choose_color_brush)

        toolbar = QToolBar()
        tools_color_brush = QToolBar()
        toolbar.setIconSize(QSize(10, 10))
        toolbar.addAction(line)
        toolbar.addAction(rect)
        toolbar.addAction(circle)
        toolbar.addAction(triangle)
        toolbar.addAction(heart)
        toolbar.addAction(star)
        toolbar.addAction(plus)

        tools_color_brush.addAction(red)
        tools_color_brush.addAction(blue)
        tools_color_brush.addAction(green)
        tools_color_brush.addAction(white)
        tools_color_brush.addAction(black)
        tools_color_brush.addAction(yellow)

        tools_color_pen = QToolBar()
        red = QAction(QIcon('redl.png'), "Красный", self)
        red.triggered.connect(self.choose_color_pen)
        green = QAction(QIcon('greenl.png'), "Зеленый", self)
        green.triggered.connect(self.choose_color_pen)
        blue = QAction(QIcon('bluel.png'), "Синий", self)
        blue.triggered.connect(self.choose_color_pen)
        white = QAction(QIcon('whitel.png'), "Белый", self)
        white.triggered.connect(self.choose_color_pen)
        black = QAction(QIcon('blackl.png'), "Черный", self)
        black.triggered.connect(self.choose_color_pen)
        yellow = QAction(QIcon('yellowl.png'), "Желтый", self)
        yellow.triggered.connect(self.choose_color_pen)
        tools_color_pen.addAction(red)
        tools_color_pen.addAction(blue)
        tools_color_pen.addAction(green)
        tools_color_pen.addAction(white)
        tools_color_pen.addAction(black)
        tools_color_pen.addAction(yellow)
        self.addToolBar(tools_color_pen)
        self.addToolBar(tools_color_brush)
        self.addToolBar(toolbar)
        self.show()

    def is_save(self):
        name, ok = QInputDialog.getText(self, 'Сохранить', 'Введите имя файла')
        if ok:
            saver.name = name
            saver.end_file()

    def is_open(self):
        name, ok = QInputDialog.getText(self, 'Открыть', 'Введите имя файла')
        if ok:
            self.main_widget = PaintWidget()
            saver.file = ''
            saver.start_file(1000, 1000)
            global figure, color_pen, color_brush, width
            res = opener.get_objects(name + ".svg")
            for obj in res:
                figure = obj.name
                self.main_widget.paint.fx = obj.x1
                self.main_widget.paint.fy = obj.y1
                if obj.name != "line":
                    color_brush = obj.brush
                color_pen = obj.pen
                width = obj.width
                if obj.name == "rect" or obj.name == "ellipse" \
                        or obj.name == "line":
                    self.main_widget.paint.sx = float(obj.x2)
                    self.main_widget.paint.sy = float(obj.y2)
                    self.main_widget.paint.tools()
                elif obj.name == "triangle":
                    self.main_widget.paint.sx = float(obj.x2)
                    self.main_widget.paint.sy = float(obj.y2)
                    self.main_widget.paint.tx = float(obj.x3)
                    self.main_widget.paint.ty = float(obj.y3)
                    self.main_widget.paint.tools()
                elif obj.name == "star" or obj.name == "plus" \
                        or obj.name == "heart":
                    self.main_widget.paint.tools()
            self.setCentralWidget(self.main_widget)

    def choose_figure(self):
        global figure
        btn = self.sender().text()
        if btn in pnt_parametres.figure.keys():
            figure = pnt_parametres.figure[btn]

    def choose_color_brush(self):
        global color_brush
        btn = self.sender().text()
        if btn in pnt_parametres.colors.keys():
            color_brush = pnt_parametres.colors[btn]

    def choose_color_pen(self):
        global color_pen
        btn = self.sender().text()
        if btn in pnt_parametres.colors.keys():
            color_pen = pnt_parametres.colors[btn]


class PaintWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.make_widget()

    def make_widget(self):
        self.resize(1500, 1500)
        grid = QGridLayout()
        self.setLayout(grid)
        self.paint = Paint()
        self.btn_clear = QPushButton('Очистить')
        self.btn_grad = QPushButton('Градиент')
        self.btn_clear.clicked.connect(self.is_clear)
        self.btn_grad.clicked.connect(self.is_grad)
        grid.addWidget(self.btn_clear)
        grid.addWidget(self.btn_grad)
        self.btn_clear.setStyleSheet('background-color: grey')
        self.btn_grad.setStyleSheet('background-color: grey')
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setFocusPolicy(Qt.NoFocus)
        self.slider.setGeometry(100, 10, 100, 30)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(10)
        self.slider.setSingleStep(1)
        self.slider.valueChanged.connect(self.width_change)
        grid.addWidget(self.slider)
        grid.addWidget(self.paint)

    def is_grad(self):
        if self.paint.gradient:
            self.paint.gradient = False
        else:
            self.paint.gradient = True

    def width_change(self, value):
        global width
        width = value

    def is_clear(self):
        self.paint.scene.clear()
        saver.file = ''
        string = saver.start_file(1000, 1000)
        saver.file += string


if __name__ == '__main__':
    string = saver.start_file(1300, 1300)
    saver.file += string
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
