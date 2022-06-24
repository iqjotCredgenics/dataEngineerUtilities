class funcTest():
    
    def __init__(self, x, y):
        try:
            self.x = int(x)
            self.y = int(y)
        except Exception:
            raise ValueError("Invalid number of input")

    def sum(self, x,y):
        return x+y

    def average(self, x,y):
        return (x+y)/2

    def power(self, x,y):
        return x**y
