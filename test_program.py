import unittest
# import figure_maker
import opener
import saver
# from PyQt5.QtCore import QPointF
# from PyQt5.QtGui import QPen, QBrush, QColor, QPolygonF, QLinearGradient
# class TestMouseClick:
#     def __init__(self, x, y):
#         self.p1 = x
#         self.p2 = y
#     def x(self):
#         return self.p1
#     def y(self):
#         return self.p2
# class Testfigure_maker(unittest.TestCase):
#     def test_make_rect_or_ell(self):
#         first = TestMouseClick(94.0, 88.0)
#         second = TestMouseClick(226.0, 189.0)
#         fx = first.x()
#         fy = first.y()
#         sx = second.x()
#         sy = second.y()
#         self.assertEqual(figure_maker.make_rect_or_ell(fx, fy, sx, sy),
#                          (94.0, 88.0, 226.0, 189.0))
#         first = TestMouseClick(364.0, 52.0)
#         second = TestMouseClick(141.0, 119.0)
#         fx = first.x()
#         fy = first.y()
#         sx = second.x()
#         sy = second.y()
#         self.assertEqual(figure_maker.make_rect_or_ell(fx, fy, sx, sy),
#                          (141.0, 52.0, 364.0, 119.0))
#         first = TestMouseClick(319.0, 226.0)
#         second = TestMouseClick(111.0, 105.0)
#         fx = first.x()
#         fy = first.y()
#         sx = second.x()
#         sy = second.y()
#         self.assertEqual(figure_maker.make_rect_or_ell(fx, fy, sx, sy),
#                          (111.0, 105.0, 319.0, 226.0))
#         first = TestMouseClick(122.0, 287.0)
#         second = TestMouseClick(371.0, 180.0)
#         fx = first.x()
#         fy = first.y()
#         sx = second.x()
#         sy = second.y()
#         self.assertEqual(figure_maker.make_rect_or_ell(fx, fy, sx, sy),
#                          (122.0, 180.0, 371.0, 287.0))
#     def test_create_rect_or_ell(self):
#         first = TestMouseClick(122.0, 287.0)
#         second = TestMouseClick(371.0, 180.0)
#         fx = first.x()
#         fy = first.y()
#         sx = second.x()
#         sy = second.y()
#         liner = QLinearGradient(QPointF(122.0, -53.5),
#                                 QPointF(371.0, -53.5))
#         liner.setColorAt(0, QColor(0, 0, 255))
#         liner.setColorAt(1, QColor(255, 0, 0))
#         brush = QBrush(liner)
#         pen = QPen(QColor(0, 0, 255), 1)
#         rect = figure_maker.create_rect_or_ell(fx, fy, sx, sy, (0, 0, 255),
#                                                (255, 0, 0), 1, True, 'rect')
#         self.assertEqual(rect[1], pen)
#         self.assertEqual(rect[2], brush)
#     def test_create_triangle(self):
#         first = TestMouseClick(122.0, 287.0)
#         second = TestMouseClick(371.0, 180.0)
#         third = TestMouseClick(220.0, 70.0)
#         fx = first.x()
#         fy = first.y()
#         sx = second.x()
#         sy = second.y()
#         tx = third.x()
#         ty = third.y()
#         liner = QLinearGradient(QPointF(122.0, 287.0), QPointF(371.0, 180.0))
#         liner.setColorAt(0, QColor(0, 0, 255))
#         liner.setColorAt(1, QColor(255, 0, 0))
#         brush = QBrush(liner)
#         pen = QPen(QColor(0, 0, 255), 5)
#         triangle = figure_maker.create_triangle(fx, fy, sx, sy, tx, ty,
#                                                 (0, 0, 255), (255, 0, 0), 5,
#                                                 True)
#         self.assertEqual(triangle[1], pen)
#         self.assertEqual(triangle[2], brush)
#     def test_make_heart(self):
#         first = TestMouseClick(122.0, 287.0)
#         fx = first.x()
#         fy = first.y()
#         heart_collection = figure_maker.make_heart(fx, fy, 5)
#         heart = heart_collection[2]
#         self.assertEqual(heart.start, QPointF(122.0, 262.0))
#         self.assertEqual(heart.p1, QPointF(157.0, 187.0))
#         self.assertEqual(heart.p2, QPointF(262.0, 262.0))
#         self.assertEqual(heart.v1, QPointF(87.0, 187.0))
#         self.assertEqual(heart.v2, QPointF(-18.0, 262.0))
#         self.assertEqual(heart.end, QPointF(122.0, 312.0))
#     def test_create_heart(self):
#         first = TestMouseClick(122.0, 287.0)
#         fx = first.x()
#         fy = first.y()
#         path1, path2 = figure_maker.create_heart(fx, fy, (0, 0, 255),
#                                                  (255, 0, 0), 2, True)
#         liner = QLinearGradient(QPointF(136.0, 247.0), QPointF(108.0, 247.0))
#         liner.setColorAt(0, QColor(0, 0, 255))
#         liner.setColorAt(1, QColor(255, 0, 0))
#         brush_expected = QBrush(liner)
#         pen_expected = QPen(QColor(0, 0, 255), 2)
#         pen, brush = path1[1], path1[2]
#         self.assertEqual(pen, pen_expected)
#         self.assertEqual(brush, brush_expected)
#     def test_create_plus(self):
#         first = TestMouseClick(122.0, 287.0)
#         fx = first.x()
#         fy = first.y()
#         plus, pen, brush = figure_maker.create_plus(fx, fy, (0, 0, 255),
#                                                     (255, 0, 0), 2, True)
#         plus_expected = QPolygonF(
#             [QPointF(120.0, 281.0), QPointF(124.0, 281.0),
#              QPointF(124.0, 285.0), QPointF(128.0, 285.0),
#              QPointF(128.0, 289.0), QPointF(124.0, 289.0),
#              QPointF(124.0, 293.0), QPointF(120.0, 293.0),
#              QPointF(120.0, 289.0), QPointF(116.0, 289.0),
#              QPointF(116.0, 285.0), QPointF(120.0, 285.0)])
#         liner = QLinearGradient(QPointF(120.0, 289.0), QPointF(124.0, 285.0))
#         liner.setColorAt(0, QColor(0, 0, 255))
#         liner.setColorAt(1, QColor(255, 0, 0))
#         brush_expected = QBrush(liner)
#         pen_expected = QPen(QColor(0, 0, 255), 2)
#         self.assertEqual(plus, plus_expected)
#         self.assertEqual(pen, pen_expected)
#         self.assertEqual(brush, brush_expected)
#     def test_create_star(self):
#         first = TestMouseClick(122.0, 287.0)
#         fx = first.x()
#         fy = first.y()
#         star, pen, brush = figure_maker.create_star(fx, fy, (0, 0, 255),
#                                                     (255, 0, 0), 2, True)
#         star_expected = QPolygonF(
#             [QPointF(122.0, 279.0), QPointF(126.0, 285.0),
#              QPointF(132.0, 285.0), QPointF(128.0, 291.0),
#              QPointF(130.0, 297.0), QPointF(122.0, 293.0),
#              QPointF(114.0, 297.0), QPointF(116.0, 291.0),
#              QPointF(112.0, 285.0), QPointF(118.0, 285.0)])
#         liner = QLinearGradient(QPointF(116.0, 291.0),
#                                 QPointF(130.0, 297.0))
#         liner.setColorAt(0, QColor(0, 0, 255))
#         liner.setColorAt(1, QColor(255, 0, 0))
#         brush_expected = QBrush(liner)
#         pen_expected = QPen(QColor(0, 0, 255), 2)
#         self.assertEqual(star, star_expected)
#         self.assertEqual(pen, pen_expected)
#         self.assertEqual(brush, brush_expected)


class Testopener(unittest.TestCase):
    def test_read_file(self):
        file = opener.read_file('test.svg')
        expected = ['123\n', '456\n', 'Это тест!']
        for real, expect in zip(file, expected):
            self.assertEqual(real, expect)

    def test_parse_rect(self):
        line = '''<rect height="37.0" width="68.0"
        y="39.0" x="70.0" stroke-width="1"
        stroke="rgb(255, 127, 255)" fill="rgb(255, 127, 255)"/>'''
        rect = opener.parse_rect(line)
        self.assertEqual(rect.x1, 70.0)
        self.assertEqual(rect.y1, 39.0)
        self.assertEqual(rect.x2, 138.0)
        self.assertEqual(rect.y2, 76.0)
        self.assertEqual(rect.brush, (255, 127, 255))
        self.assertEqual(rect.pen, (255, 127, 255))
        self.assertEqual(rect.width, 1)

    def test_parse_ell(self):
        line = '''<ellipse cx="142.0" cy="232.5" rx="46.0" ry="31.5"
        fill="rgb(255, 0, 0)" stroke-width="1" stroke="rgb(0, 0, 0)"/>'''
        ell = opener.parse_ell(line)
        self.assertEqual(ell.x1, 96.0)
        self.assertEqual(ell.y1, 201.0)
        self.assertEqual(ell.x2, 188.0)
        self.assertEqual(ell.y2, 264.0)
        self.assertEqual(ell.brush, (255, 0, 0))
        self.assertEqual(ell.pen, (0, 0, 0))
        self.assertEqual(ell.width, 1)

    def test_parse_line(self):
        line = '''<line x1="199.0" y1="76.0" x2="143.0" y2="128.0"
        stroke-width="1" stroke="rgb(255, 127, 255)"/>'''
        line = opener.parse_line(line)
        self.assertEqual(line.x1, 199.0)
        self.assertEqual(line.y1, 76.0)
        self.assertEqual(line.x2, 143.0)
        self.assertEqual(line.y2, 128.0)
        self.assertEqual(line.pen, (255, 127, 255))
        self.assertEqual(line.width, 1)

    def test_parse_triang(self):
        line = '''<polygon points="294.0,140.0 373.0,157.0 302.0,276.0"
        fill="rgb(0, 0, 255)" stroke-width="5" stroke="rgb(255, 0, 0)"/>'''
        triang = opener.parse_triang(line)
        self.assertEqual(triang.x1, 294.0)
        self.assertEqual(triang.y1, 140.0)
        self.assertEqual(triang.x2, 373.0)
        self.assertEqual(triang.y2, 157.0)
        self.assertEqual(triang.x3, 302.0)
        self.assertEqual(triang.y3, 276.0)
        self.assertEqual(triang.brush, (0, 0, 255))
        self.assertEqual(triang.pen, (255, 0, 0))
        self.assertEqual(triang.width, 5)

    def test_parse_heart(self):
        line = '''<path id="svg_1" d="    M 215.0,332.0    C 250.0,257.0
        355.0,332.0      215.0,382.0    M 215.0,332.0    C 180.0,257.0
        75.0,332.0      215.0,382.0"      fill="rgb(0, 0, 255)"
        stroke="rgb(255, 0, 0)"       stroke-width="5"/>'''
        heart = opener.parse_heart(line)
        self.assertEqual(heart.x1, 215.0)
        self.assertEqual(heart.y1, 357.0)
        self.assertEqual(heart.brush, (0, 0, 255))
        self.assertEqual(heart.pen, (255, 0, 0))
        self.assertEqual(heart.width, 5)

    def test_parse_star(self):
        line = '''<polygon points="442.0,71.0 452.0,86.0 467.0,86.0
        457.0,101.0 462.0,116.0 442.0,106.0 422.0,116.0 427.0,101.0 417.0,86.0
        432.0,86.0" fill="rgb(0, 0, 255)" stroke-width="5"
        stroke="rgb(255, 0, 0)"/>'''
        star = opener.parse_star(line)
        self.assertEqual(star.x1, 442.0)
        self.assertEqual(star.y1, 91.0)
        self.assertEqual(star.brush, (0, 0, 255))
        self.assertEqual(star.pen, (255, 0, 0))
        self.assertEqual(star.width, 5)

    def test_parse_plus(self):
        line = '''<polygon points="310.0,61.0 320.0,61.0 320.0,71.0 330.0,71.0
        330.0,81.0 320.0,81.0 320.0,91.0 310.0,91.0 310.0,81.0 300.0,81.0
        300.0,71.0 310.0,71.0" fill="rgb(0, 0, 255)" stroke-width="5"
        stroke="rgb(255, 0, 0)"/>'''
        star = opener.parse_plus(line)
        self.assertEqual(star.x1, 315.0)
        self.assertEqual(star.y1, 76.0)
        self.assertEqual(star.brush, (0, 0, 255))
        self.assertEqual(star.pen, (255, 0, 0))
        self.assertEqual(star.width, 5)

    def test_get_pen(self):
        line = '''<polygon points="310.0,61.0 320.0,61.0 320.0,71.0 330.0,71.0
        330.0,81.0 320.0,81.0 320.0,91.0 310.0,91.0 310.0,81.0 300.0,81.0
        300.0,71.0 310.0,71.0" fill="rgb(0, 0, 255)" stroke-width="5"
        stroke="rgb(255, 0, 0)"/>'''
        pen = opener.get_pen(line)
        self.assertEqual(pen, (255, 0, 0))

    def test_get_brush(self):
        line = '''<polygon points="310.0,61.0 320.0,61.0 320.0,71.0 330.0,71.0
        330.0,81.0 320.0,81.0 320.0,91.0 310.0,91.0 310.0,81.0 300.0,81.0
        300.0,71.0 310.0,71.0" fill="rgb(0, 0, 255)" stroke-width="5"
        stroke="rgb(255, 0, 0)"/>'''
        brush = opener.get_brush(line)
        self.assertEqual(brush, (0, 0, 255))

    def test_get_width(self):
        line = '''<polygon points="310.0,61.0 320.0,61.0 320.0,71.0 330.0,71.0
        330.0,81.0 320.0,81.0 320.0,91.0 310.0,91.0 310.0,81.0 300.0,81.0
        300.0,71.0 310.0,71.0" fill="rgb(0, 0, 255)" stroke-width="5"
        stroke="rgb(255, 0, 0)"/>'''
        width = opener.get_width(line)
        self.assertEqual(width, 5)

    def test_find_figure(self):
        lines = opener.read_file('test2.svg')
        names = ['rect', 'line', 'ellipse', 'triangle', 'heart', 'star',
                 'plus']
        gen_lines = opener.find_figure(lines)
        for line, figure in zip(gen_lines, names):
            self.assertEqual(line.name, figure)

    def test_get_objects(self):
        objects = opener.get_objects('test2.svg')
        names = ['rect', 'line', 'ellipse', 'triangle', 'heart', 'star',
                 'plus']
        for obj, figure in zip(objects, names):
            self.assertEqual(obj.name, figure)


class Testsaver(unittest.TestCase):
    def test_start_file(self):
        text = saver.start_file('1300', '1300')
        expected = '''<svg version="1.1"
     baseProfile="full"
     xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     xmlns:ev="http://www.w3.org/2001/xml-events"
     width="1300" height="1300">\n'''
        self.assertEqual(text, expected)

    def test_save_line(self):
        expected = '<line x1="199.0" y1="76.0" x2="143.0" y2="128.0"' \
                   ' stroke-width="1" stroke="rgb(255, 127, 255)"/>'
        expected = expected.replace("\n", "") + "\n"
        line = saver.save_line(199.0, 76.0, 143.0, 128.0, 1, (255, 127, 255))
        self.assertEqual(line, expected)

    def test_save_rect(self):
        expected = '<rect height="37.0" width="68.0" y="39.0" x="70.0"' + \
                   ' stroke-width="1" stroke="rgb(255, 127, 255)"' + \
                   ' fill="rgb(255, 127, 255)"/>'
        expected = expected.replace("\n", "") + "\n"
        rect = saver.save_rect(70.0, 39.0, 138.0, 76.0, 1, (255, 127, 255),
                               (255, 127, 255))
        self.assertEqual(rect, expected)

    def test_save_ell(self):
        expected = '<ellipse cx="142.0" cy="232.5" rx="46.0" ry="31.5" ' + \
            'fill="rgb(255, 0, 0)" stroke-width="1" stroke="rgb(0, 0, 0)"/>'
        expected = expected.replace("\n", "") + "\n"
        ell = saver.save_ellipse(96.0, 201.0, 188.0, 264.0, 1, (255, 0, 0),
                                 (0, 0, 0))
        self.assertEqual(ell, expected)

    def test_save_triangle(self):
        expected = '<polygon points="294.0,140.0 373.0,157.0 302.0,276.0"' +\
                   ' fill="rgb(0, 0, 255)" stroke-width="5"' + \
                   ' stroke="rgb(255, 0, 0)"/>'''
        expected = expected.replace("\n", "") + "\n"
        triangle = saver.save_triangle(294.0, 140.0, 373.0, 157.0, 302.0,
                                       276.0, 5, (0, 0, 255), (255, 0, 0))
        self.assertEqual(triangle, expected)

    def test_save_star(self):
        expected = '<polygon points="442.0,71.0 452.0,86.0 467.0,86.0' + \
                   ' 457.0,101.0 462.0,116.0 442.0,106.0 422.0,116.0' + \
                   ' 427.0,101.0 417.0,86.0 432.0,86.0"' + \
                   ' fill="rgb(0, 0, 255)" stroke-width="5"' + \
                   ' stroke="rgb(255, 0, 0)"/>'
        expected = expected.replace("\n", "") + "\n"
        star = saver.save_star(442.0, 71.0, 452.0, 86.0, 467.0, 86.0,
                               457.0, 101.0, 462.0, 116.0, 442.0, 106.0,
                               422.0, 116.0, 427.0, 101.0, 417.0, 86.0,
                               432.0, 86.0, pen=(255, 0, 0),
                               brush=(0, 0, 255), width=5)
        self.assertEqual(star, expected)
    # def test_save_heart(self):
    #     expected = '<path id="svg_1" d="M 215.0,332.0 C 250.0,257.0' + \
    #                ' 355.0,332.0 215.0,382.0 M 215.0,332.0' + \
    #                ' C 180.0,257.0 75.0,332.0 215.0,382.0"' + \
    #                ' fill="rgb(0, 0, 255)" stroke="rgb(255, 0, 0)"' + \
    #                ' stroke-width="5"/>'
    #     expected = expected.replace("\n", "") + "\n"
    #     heart = figure_maker.Heart()
    #     heart.start = QPointF(215.0, 332.0)
    #     heart.p1 = QPointF(250.0, 257.0)
    #     heart.p2 = QPointF(355.0, 332.0)
    #     heart.v1 = QPointF(180.0, 257.0)
    #     heart.v2 = QPointF(75.0, 332.0)
    #     heart.end = QPointF(215.0, 382.0)
    #     heart_save = saver.save_heart(heart, 5, (0, 0, 255), (255, 0, 0))
    #     self.assertEqual(heart_save, expected)

    def test_save_plus(self):
        expected = '<polygon points="310.0,61.0 320.0,61.0 320.0,71.0' + \
                   ' 330.0,71.0 330.0,81.0 320.0,81.0 320.0,91.0' + \
                   ' 310.0,91.0 310.0,81.0 300.0,81.0 300.0,71.0' + \
                   ' 310.0,71.0" fill="rgb(0, 0, 255)" stroke-width="5"' + \
                   ' stroke="rgb(255, 0, 0)"/>'
        expected = expected.replace("\n", "") + "\n"
        plus = saver.save_plus(310.0, 61.0, 320.0, 61.0, 320.0, 71.0, 330.0,
                               71.0, 330.0, 81.0, 320.0, 81.0, 320.0, 91.0,
                               310.0, 91.0, 310.0, 81.0, 300.0, 81.0, 300.0,
                               71.0, 310.0, 71.0, pen=(255, 0, 0),
                               brush=(0, 0, 255), width=5)
        self.assertEqual(plus, expected)

    def test_end_file(self):
        saver.file = ''
        saver.name = 'test3'
        saver.end_file()
        with open("test3.svg") as file:
            lines = file.readlines()
        self.assertEqual(lines[0], '</svg>\n')


if __name__ == "__main__":
    unittest.main()
