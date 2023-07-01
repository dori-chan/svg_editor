name = ''
file = ''


def start_file(width, height):
    """Заполняет начало изображения в svg формате"""
    start = """<svg version="1.1"
     baseProfile="full"
     xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     xmlns:ev="http://www.w3.org/2001/xml-events"
     width="{0}" height="{1}">\n""".format(width, height)
    return start


def save_line(x1, x2, y1, y2, width, brush_color):
    """"Сохраняет примитив 'Линия'"""
    line = '<line x1="{0}" y1="{1}" x2="{2}" y2="{3}"' + \
           ' stroke-width="{width}" stroke="rgb{4}"/>\n'
    line = line.format(x1, x2, y1, y2, brush_color, width=width)
    line = line.replace('\n', '')
    return line+"\n"


def save_rect(x1, y1, x2, y2, width_cont, brush_color, pen_color):
    """"Сохраняет примитив 'Прямоугольник'"""
    width = x2 - x1
    height = y2 - y1
    rect = '<rect height="{height}" width="{width}"' + \
           ' y="{0}" x="{1}" stroke-width="{width_cont}"' + \
           ' stroke="rgb{pen_color}" fill="rgb{brush_color}"/>\n'
    rect = rect.format(y1, x1, width_cont=width_cont, width=width,
                       height=height, brush_color=brush_color,
                       pen_color=pen_color)
    rect = rect.replace('\n', '')
    return rect+"\n"


def save_ellipse(x1, y1, x2, y2, width_cont, brush_color, pen_color):
    """"Сохраняет примитив 'Эллипс'"""
    width = x2 - x1
    height = y2 - y1
    cx = x1 + width / 2
    cy = y1 + height / 2
    rx = width / 2
    ry = height / 2
    ell = '<ellipse cx="{0}" cy="{1}" rx="{2}" ry="{3}"' + \
          ' fill="rgb{brush_color}" stroke-width="{width_cont}"' + \
          ' stroke="rgb{pen_color}"/>\n'
    ell = ell.format(cx, cy, rx, ry, width_cont=width_cont,
                     brush_color=brush_color,
                     pen_color=pen_color)
    ell = ell.replace('\n', '')
    return ell+"\n"


def save_heart(heart, width, brush_color, pen_color):
    start = heart.start
    p1 = heart.p1
    p2 = heart.p2
    v1 = heart.v1
    v2 = heart.v2
    end = heart.end
    heart1 = '<path id="svg_1" d="M {0},{1} C {2},{3} {4},{5}' + \
             ' {6},{7} M {0},{1} C {8},{9} {10},{11} {6},{7}"' + \
             ' fill="rgb{brush_color}" stroke="rgb{pen_color}"' + \
             ' stroke-width="{width}"/>'
    heart1 = heart1.format(start.x(), start.y(), p1.x(), p1.y(),
                           p2.x(), p2.y(), end.x(), end.y(),
                           v1.x(), v1.y(), v2.x(), v2.y(),
                           width=width, brush_color=brush_color,
                           pen_color=pen_color)
    heart1 = heart1.replace('\n', '')
    return heart1+"\n"


def save_plus(*args, pen, brush, width):
    plus = '<polygon points="{},{} {},{} {},{} {},{} {},{}' + \
           ' {},{} {},{} {},{} {},{} {},{} {},{} {},{}"' + \
           ' fill="rgb{brush_color}" stroke-width="{width}"' + \
           ' stroke="rgb{pen_color}"/>'
    plus = plus.format(*args, brush_color=brush,
                       pen_color=pen, width=width)
    plus = plus.replace('\n', '')
    return plus + "\n"


def save_star(*args, pen, brush, width):
    star = '<polygon points="{},{} {},{} {},{} {},{} {},{}' + \
           ' {},{} {},{} {},{} {},{} {},{}"' + \
           ' fill="rgb{brush_color}" stroke-width="{width}"' + \
           ' stroke="rgb{pen_color}"/>'
    star = star.format(*args, brush_color=brush,
                       pen_color=pen, width=width)
    star = star.replace('\n', '')
    return star + "\n"


def save_triangle(x1, y1, x2, y2, x3, y3, width, brush_color, pen_color):
    """"Сохраняет примитив 'Треугольник'"""
    triang = '<polygon points="{0},{1} {2},{3} {4},{5}"' + \
             ' fill="rgb{brush_color}" stroke-width="{width}"' + \
             ' stroke="rgb{pen_color}"/>\n'
    triang = triang.format(x1, y1, x2, y2, x3, y3,
                           brush_color=brush_color,
                           width=width,
                           pen_color=pen_color)
    triang = triang.replace('\n', '')
    return triang+"\n"


def end_file():
    """"Завершает сохранение изображения и записывает его в файл"""
    global file
    file += '</svg>\n'
    with open(name + '.svg', 'w') as f:
        f.write(file)
    file = file[:-7]
