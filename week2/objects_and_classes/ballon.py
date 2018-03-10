class Ballon(object): #ballon class
    def __init__(self, color, size, shape):
        self.color = color
        self.size = size
        self.shape = shape
        self.inflated = False
        self.work = True
        

def inflate(self):
    if self.work:
        self.inflated = True
    else:
        print "You exploded this ballon idiot."

def explode(self):
    self.explode = False
    self.work = False
    print "BANG!"

def deflate(self):
    self.inflated = False

ballon1 = Ballon('red', 'big', 'round')
ballon2 = Ballon('blue', 'small', 'square')
   