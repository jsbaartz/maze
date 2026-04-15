from graphics import Line, Point


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1

        self.__win = win

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        if self.__win is None:
            return

        bg_color = self.__win.get_bg_color()

        left_color = "black" if self.has_left_wall else bg_color
        right_color = "black" if self.has_right_wall else bg_color
        top_color = "black" if self.has_top_wall else bg_color
        bottom_color = "black" if self.has_bottom_wall else bg_color

        self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), left_color)
        self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), right_color)
        self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), top_color)
        self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), bottom_color)

    def draw_move(self, to_cell, undo=False):
        x1 = (self.__x1 + self.__x2) / 2
        y1 = (self.__y1 + self.__y2) / 2

        x2 = (to_cell._Cell__x1 + to_cell._Cell__x2) / 2
        y2 = (to_cell._Cell__y1 + to_cell._Cell__y2) / 2

        if self.__win is None:
            return

        color = "gray" if undo else "red"
        self.__win.draw_line(Line(Point(x1, y1), Point(x2, y2)), color)