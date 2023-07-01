import re


class FigureParametres:
    def __init__(self, x1, y1, width, pen, name):
        self.x1 = float(x1)
        self.x2 = 0
        self.y1 = float(y1)
        self.y2 = 0
        self.width = int(width)
        self.pen = pen
        self.brush = (0, 0, 0,)
        self.name = name


def get_objects(filename):
    """Возвращает список найденных фигур и их параметров"""
    lines = read_file(filename)
    generate_obj = find_figure(lines)
    list_of_obj = list()
    for obj in generate_obj:
        list_of_obj.append(obj)
    return list_of_obj


def find_figure(lines):
    """Ищет в изображении определенные фигуры"""
    for line in lines:
        mo = re.search("<rect.+?/>", line)
        if mo:
            yield parse_rect(line)
            continue
        mo = re.search("<line.+?/>", line)
        if mo:
            yield parse_line(line)
        mo = re.search("<ellipse.+?/>", line)
        if mo:
            yield parse_ell(line)
        mo = re.search("<polygon.+?/>", line)
        if mo:
            mo = re.findall(r'[\d]+?\.[\d]+?,[\d]+?\.[\d]+?', line)
            if len(mo) == 3:
                yield parse_triang(line)
            elif len(mo) == 10:
                yield parse_star(line)
            elif len(mo) == 12:
                yield parse_plus(line)
        mo = re.search("<path.+?/>", line)
        if mo:
            yield parse_heart(line)


def parse_star(line):
    """Разбивает на составляющие звезду"""
    points = re.search(r'[\d]+?\.[\d]+?,[\d]+?\.[\d]+?', line).group(0)
    points = points.split(",")
    width = int(get_width(line))
    x = float(points[0])
    y = float(points[1])
    x = x
    y = y + (4 * width)
    figure = FigureParametres(x, y, width, get_pen(line), "star")
    figure.brush = get_brush(line)
    return figure


def parse_plus(line):
    """Разбивает на составляющие плюс"""
    points = re.search(r'[\d]+?\.[\d]+?,[\d]+?\.[\d]+?', line).group(0)
    points = points.split(",")
    width = int(get_width(line))
    x = float(points[0])
    y = float(points[1])
    x = x + width
    y = y + (3 * width)
    figure = FigureParametres(x, y, width, get_pen(line), "plus")
    figure.brush = get_brush(line)
    return figure


def parse_heart(line):
    """Разбивает на составляющие сердце"""
    point = re.search(r'M ([\d]+?\.[\d]+?,[\d]+?\.[\d]+?)', line).group(1)
    point = point.split(",")
    x = float(point[0])
    y = float(point[1])
    width = int(get_width(line))
    x = x
    y = y + (5 * width)

    figure = FigureParametres(x, y, width, get_pen(line), "heart")
    figure.brush = get_brush(line)
    return figure


def parse_triang(line):
    """Разбивает на составляющие треугольник"""
    points = re.search(r'points="([\d.,\s]+?)"', line).group(1)
    points = points.split(" ")
    for i in range(len(points)):
        points[i] = points[i].split(",")
    x1 = points[0][0]
    y1 = points[0][1]
    figure = FigureParametres(x1, y1, get_width(line), get_pen(line),
                              "triangle")
    figure.x2 = float(points[1][0])
    figure.y2 = float(points[1][1])
    figure.x3 = float(points[2][0])
    figure.y3 = float(points[2][1])
    figure.brush = get_brush(line)
    return figure


def parse_ell(line):
    """Разбивает на составляющие эллипс"""
    cx = float(re.search(r'cx="([\d.]+?)"', line).group(1))
    cy = float(re.search(r'cy="([\d.]+?)"', line).group(1))
    rx = float(re.search(r'rx="([\d.]+?)"', line).group(1))
    ry = float(re.search(r'ry="([\d.]+?)"', line).group(1))

    width = int(rx * 2)
    height = int(ry * 2)
    x1 = cx - rx
    y1 = cy - ry
    x2 = width + x1
    y2 = height + y1

    figure = FigureParametres(x1, y1, get_width(line), get_pen(line),
                              'ellipse')
    figure.x2 = x2
    figure.y2 = y2
    figure.brush = get_brush(line)
    return figure


def parse_rect(line):
    """Разбивает на составляющие прямоугольник"""
    height = re.search(r'height="([\d.]+?)"', line).group(1)
    width = re.search(r'width="([\d.]+?)"', line).group(1)
    x = re.search(r'x="([\d.]+?)"', line).group(1)
    y = re.search(r'y="([\d.]+?)"', line).group(1)

    x2 = float(width) + float(x)
    y2 = float(height) + float(y)

    figure = FigureParametres(x, y, get_width(line), get_pen(line), 'rect')
    figure.x2 = x2
    figure.y2 = y2
    figure.brush = get_brush(line)
    return figure


def parse_line(line):
    """Разбивает на составляющие линию"""
    width = re.search(r'width="([\d.]+?)"', line).group(1)
    pen = get_pen(line)
    x1 = re.search(r'x1="([\d.]+?)"', line).group(1)
    x2 = float(re.search(r'x2="([\d.]+?)"', line).group(1))
    y1 = re.search(r'y1="([\d.]+?)"', line).group(1)
    y2 = float(re.search(r'y2="([\d.]+?)"', line).group(1))

    figure = FigureParametres(x1, y1, width, pen, 'line')
    figure.x2 = x2
    figure.y2 = y2
    return figure


def get_pen(line):
    """Достает цвет обводки"""
    pen = re.search(r'stroke="rgb(\([\d\s,]+?\))"', line)
    if pen:
        return tuple([int(x) for x in pen.group(1)[1:-1].split(", ")])


def get_brush(line):
    """Достает цвет кисти"""
    brush = re.search(r'fill="rgb(\([\d\s,]+?\))"', line)
    if brush:
        return tuple([int(x) for x in brush.group(1)[1:-1].split(", ")])


def get_width(line):
    """Достает ширину обводки"""
    width = re.search(r'stroke-width="([\d.]+?)"', line)
    if width:
        return int(width.group(1))


def read_file(filename):
    """Считывает построчно файл"""
    with open(filename) as file:
        for line in file:
            yield line
