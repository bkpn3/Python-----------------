class Rectangle:

    def __init__(self, left_top, right_bottom):
        self.left_top = left_top
        self.right_bottom = right_bottom
        
    def perimeter(self):
        width = self.right_bottom[0] - self.left_top[0]
        height = self.right_bottom[1] - self.left_top[1]
        return round((width + height) * 2, 2)
        
    def area(self):
        width = abs(self.right_bottom[0] - self.left_top[0])
        height = abs(self.right_bottom[1] - self.left_top[1])
        return round(width * height, 2)

rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())

rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())