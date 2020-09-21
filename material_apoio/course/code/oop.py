import math 

class Geometry:
    def __init__(self):
        self.epsg = 3116
        self.type = "Unknown"
    
    def print_details(self):
        print("EPSG: {}, TYPE: {}, VALID: {}".format(self.epsg, self.type, self.is_valid()))

    def is_valid(self):
        return False
        
        
class Point(Geometry):
    def __init__(self, x=None, y=None):
        super().__init__()
        self.x = x
        self.y = y
        self.type = "Point"
        
    def distance_to_point(self, point2):
        return math.sqrt((point2.x - self.x) ** 2 + (point2.y - self.y) ** 2)

    def is_valid(self):
        if self.x is None or self.y is None:
            return False

        return True
        

# Create a point and print its details
p1 = Point(10,10)
p1.print_details()

# Create another point and get distance between point 1 and point 2
p2 = Point(15, 15)
print("Distance to second point: {}".format(p2.distance_to_point(p1)))



class Line(Geometry):
    def __init__(self, point1=Point(), point2=Point()):
        super().__init__()
        self.points = [point1, point2]
        self.type = "Line"
    
    def length(self):
        if self.is_valid():
            return self.points[0].distance_to_point(self.points[1])
        else:
            return None

    def is_valid(self):
        if not(self.points[0] is None or self.points[1] is None):
            return self.points[0].is_valid() and self.points[1].is_valid()
        else:
            return False
        
        
# Crear clase Line que reciba 2 puntos (inicio y fin) y crear método length()
line = Line(p1, p2)
line.print_details()
print("Line length: {}".format(line.length()))
