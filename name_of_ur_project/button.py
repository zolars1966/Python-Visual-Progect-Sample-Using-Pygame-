class Button:
    def __init__(self, point1, point2):
        self.x1, self.y1 = self.point1 = point1
        self.x2, self.y2 = self.point2 = point2
        self.coords = [[self.x1, self.y1], [self.x2, self.y1], [self.x2, self.y2], [self.x1, self.y2]]
        self.state = "unpressed"
        self.is_pressed = False

    def coll(self, mouse_pos):
        if self.x1 <= mouse_pos[0] <= self.x2:
            if self.y1 <= mouse_pos[1] <= self.y2:
                self.state = "pressed" if self.state == "unpressed" else "unpressed"
                self.is_pressed = not self.is_pressed
                return True
        return False
