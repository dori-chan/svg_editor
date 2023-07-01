from PyQt5.QtCore import QPointF, QRectF
from PyQt5.QtGui import QPen, QBrush, QColor, QPolygonF, QPainterPath, \
    QLinearGradient
import saver


class Heart:
    def __init__(self):
        self.start = 0
        self.p1 = 0
        self.p2 = 0
        self.v1 = 0
        self.v2 = 0
        self.end = 0


def make_rect_or_ell(fx, fy, sx, sy):
    """Возвращает координаты, по которым будет строиться прямоугольник/
    эллипс на сцене"""
    left_up_x = fx
    left_up_y = fy
    right_bot_x = sx
    right_bot_y = sy
    if left_up_x > right_bot_x:
        left_up_x, right_bot_x = right_bot_x, left_up_x
    if left_up_y > right_bot_y:
        left_up_y, right_bot_y = right_bot_y, left_up_y
    return left_up_x, left_up_y, right_bot_x, right_bot_y


def create_rect_or_ell(fx, fy, sx, sy, color_pen, color_brush, width,
                       gradient, figure):
    """Создает прямоугольник или эллипс и контуры и кисти для них"""
    pen = QPen(QColor(color_pen[0], color_pen[1], color_pen[2]), width)
    brush = QBrush(QColor(color_brush[0], color_brush[1], color_brush[2]))
    if gradient:
        if fx < sx:
            liner = QLinearGradient(QPointF(fx, (sy - fy) / 2),
                                    QPointF(sx, (sy - fy) / 2))
        else:
            liner = QLinearGradient(QPointF(sx, (sy - fy) / 2),
                                    QPointF(fx, (sy - fy) / 2))
        liner.setColorAt(0, QColor(*color_pen))
        liner.setColorAt(1, QColor(*color_brush))
        brush = QBrush(liner)
    cords = make_rect_or_ell(fx, fy, sx, sy)
    rect = QRectF(QPointF(cords[0], cords[1]), QPointF(cords[2], cords[3]))
    if figure == 'rect':
        saves = saver.save_rect(cords[0], cords[1], cords[2], cords[3], width,
                                color_brush, color_pen)
    else:
        saves = saver.save_ellipse(cords[0], cords[1], cords[2], cords[3],
                                   width, color_brush, color_pen)
    saver.file += saves
    return rect, pen, brush


def create_triangle(fx, fy, sx, sy, tx, ty, color_pen, color_brush, width,
                    gradient):
    """Создает треугольник, контур и кисть для него"""
    pen = QPen(QColor(color_pen[0], color_pen[1], color_pen[2]), width)
    brush = QBrush(QColor(color_brush[0], color_brush[1], color_brush[2]))
    if gradient:
        liner = QLinearGradient(QPointF(fx, fy), QPointF(sx, sy))
        liner.setColorAt(0, QColor(*color_pen))
        liner.setColorAt(1, QColor(*color_brush))
        brush = QBrush(liner)
    triangle = QPolygonF([QPointF(fx, fy), QPointF(sx, sy), QPointF(tx, ty)])
    saves = saver.save_triangle(fx, fy, sx,
                                sy, tx, ty, width, color_brush, color_pen)
    saver.file += saves
    return triangle, pen, brush


def create_heart(fx, fy, color_pen, color_brush, width, gradient):
    """Создает сердце, контур и кисть для него"""
    pen = QPen(QColor(color_pen[0], color_pen[1], color_pen[2]), width)
    brush = QBrush(QColor(color_brush[0], color_brush[1], color_brush[2]))
    path1, path2, heart = make_heart(fx, fy, width)
    if gradient:
        liner = QLinearGradient(heart.p1, heart.v1)
        liner.setColorAt(0, QColor(*color_pen))
        liner.setColorAt(1, QColor(*color_brush))
        brush = QBrush(liner)
    path1 = path1, pen, brush
    path2 = path2, pen, brush
    saves = saver.save_heart(heart, width=width, brush_color=color_brush,
                             pen_color=color_pen)
    saver.file += saves
    return path1, path2


def make_heart(fx, fy, width):
    """Создает и возвращает две кривые, по которым строится сердце"""
    heart = Heart()
    heart.start = QPointF(fx, fy - (5*width))
    heart.end = QPointF(fx, fy + (5*width))
    heart.p1 = QPointF(fx + (7*width), fy - (20*width))
    heart.p2 = QPointF(fx + (28*width), fy + (-5*width))
    cubic_path1 = QPainterPath(heart.start)
    cubic_path1.cubicTo(heart.p1, heart.p2, heart.end)

    step = heart.p1.x() - fx
    heart.v1 = QPointF(fx - step, heart.p1.y())
    step = heart.p2.x() - fx
    heart.v2 = QPointF(fx - step, heart.p2.y())
    cubic_path2 = QPainterPath(heart.start)
    cubic_path2.cubicTo(heart.v1,  heart.v2, heart.end)
    return cubic_path1, cubic_path2, heart


def create_star(fx, fy, color_pen, color_brush, width, gradient):
    """Создает звезду, контур и кисти для нее"""
    pen = QPen(QColor(color_pen[0], color_pen[1], color_pen[2]), width)
    brush = QBrush(QColor(color_brush[0], color_brush[1], color_brush[2]))

    x1, y1 = fx, fy - (4 * width)
    x2, y2 = fx + (2 * width), fy - (1 * width)
    x3, y3 = fx + (5 * width), fy - (1 * width)
    x4, y4 = fx + (3 * width), fy + (2 * width)
    x5, y5 = fx + (4 * width), fy + (5 * width)
    x6, y6 = fx, fy + (3 * width)
    x7, y7 = fx - (4 * width), fy + (5 * width)
    x8, y8 = fx - (3 * width), fy + (2 * width)
    x9, y9 = fx - (5 * width), fy - width
    x10, y10 = fx - (2 * width), fy - width
    star = QPolygonF(
        [QPointF(x1, y1), QPointF(x2, y2), QPointF(x3, y3), QPointF(x4, y4),
         QPointF(x5, y5), QPointF(x6, y6), QPointF(x7, y7), QPointF(x8, y8),
         QPointF(x9, y9), QPointF(x10, y10)])
    if gradient:
        liner = QLinearGradient(QPointF(fx - (3 * width), fy + (2 * width)),
                                QPointF(fx + (4 * width), fy + (5 * width)))
        liner.setColorAt(0, QColor(*color_pen))
        liner.setColorAt(1, QColor(*color_brush))
        brush = QBrush(liner)
    saves = saver.save_star(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6,
                            y6, x7, y7, x8, y8, x9, y9, x10, y10,
                            pen=color_pen, brush=color_brush,
                            width=width)
    saver.file += saves
    return star, pen, brush


def create_plus(fx, fy, color_pen, color_brush, width, gradient):
    """Создает плюс, контур и кисть для него"""
    pen = QPen(QColor(color_pen[0], color_pen[1], color_pen[2]), width)
    brush = QBrush(QColor(color_brush[0], color_brush[1], color_brush[2]))

    x1, y1 = fx - width, fy - (3 * width)
    x2, y2 = fx + width, fy - (3 * width)
    x3, y3 = fx + width, fy - width
    x4, y4 = fx + (3 * width), fy - width
    x5, y5 = fx + (3 * width), fy + width
    x6, y6 = fx + width, fy + width
    x7, y7 = fx + width, fy + (3 * width)
    x8, y8 = fx - width, fy + (3 * width)
    x9, y9 = fx - width, fy + width
    x10, y10 = fx - (3 * width), fy + width
    x11, y11 = fx - (3 * width), fy - width
    x12, y12 = fx - width, fy - width
    plus = QPolygonF(
        [QPointF(x1, y1), QPointF(x2, y2), QPointF(x3, y3),
         QPointF(x4, y4), QPointF(x5, y5), QPointF(x6, y6),
         QPointF(x7, y7), QPointF(x8, y8), QPointF(x9, y9),
         QPointF(x10, y10), QPointF(x11, y11), QPointF(x12, y12)])
    if gradient:
        liner = QLinearGradient(QPointF(fx - width, fy + width),
                                QPointF(fx + width, fy - width))
        liner.setColorAt(0, QColor(*color_pen))
        liner.setColorAt(1, QColor(*color_brush))
        brush = QBrush(liner)
    saves = saver.save_plus(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6,
                            y6, x7, y7, x8, y8, x9, y9, x10, y10, x11,
                            y11, x12, y12, pen=color_pen,
                            brush=color_brush, width=width)
    saver.file += saves
    return plus, pen, brush
