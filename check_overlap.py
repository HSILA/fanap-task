from ast import literal_eval
import pickle
import os

class Rectangle:
    """
    We consider four coordinates of a rectangle like this:
    ul ........... ur
    .              .
    .              .
    ll ........... lr
    """
    def __init__(self, ul, lr):
        self.ul = ul
        self.lr = lr

class Overlap:
    def get_rectangle(self, dictionary):
        return Rectangle(
                        (dictionary['x'], dictionary['y']),
                        (dictionary['x'] + dictionary['width'], dictionary['y'] - dictionary['height'])
                        )

    def parse_json(self, json):
        if type(json) is str:
            json = literal_eval(json)
        return json

    def doOverlap(self, rect1, rect2):
        """
        Check if two rectangles overlap
        """
        # To check if either rectangle is actually a line
        # For example  :  l1 ={-1,0}  r1={1,1}  l2={0,-1}  r2={0,1}
        if (rect1.ul[0] == rect1.lr[0] or rect1.ul[1] == rect1.lr[1] or rect2.ul[0] == rect2.lr[0] or rect2.ul[1] == rect2.lr[1]):
            # The line cannot have positive overlap    
            return False

        # If one rectangle is on left side of other
        if(rect1.ul[0] >= rect2.lr[0] or rect2.ul[0] >= rect1.lr[0]):
            return False
 
        # If one rectangle is above other
        if(rect1.lr[1] >= rect2.ul[1] or rect2.lr[1] >= rect1.ul[1]):
            return False

        return True

    def write_file(self, rectangle):
        file_name = 'rectangles.pkl'
        if os.path.isfile(file_name):
            with open(file_name, 'rb') as f:
                rectangles = pickle.load(f)
            rectangles.append(rectangle)
            with open(file_name, 'wb') as f:
                pickle.dump(rectangles, f)
        else:
            rectangles = [rectangle]
            with open(file_name, 'wb') as f:
                pickle.dump(rectangles, f)

    def __init__(self, json, time):
        self.json = self.parse_json(json)
        self.time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.main_rectangle = self.get_rectangle(self.json['main'])
        self.rectangles = []
        for rectangle in self.json['input']:
            self.rectangles.append(rectangle)

        for rectangle in self.rectangles:
            if self.doOverlap(self.main_rectangle, self.get_rectangle(rectangle)):
                rectangle['time'] = self.time
                self.write_file(rectangle)