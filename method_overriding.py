class Shape: # Parent class
    def draw(self):
        print("Drawing shape")
        
class Circle(Shape): # Child class
    def draw(self):  # Overriding parent method
        print("Drawing Circle")
        
# s = Shape()
# s.draw()   # Output: Drawing shape

c = Circle()
c.draw()   # Output: Drawing Circle because the chi;d class method overrides the parent class method.