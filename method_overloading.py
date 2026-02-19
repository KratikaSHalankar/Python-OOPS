class Calculator:
    def multiply(self, a, b, c=1):  # default parameter
        print(a * b * c)

c = Calculator()
c.multiply(10, 10)      # Output: 100
c.multiply(10, 10, 10)  # Output: 1000