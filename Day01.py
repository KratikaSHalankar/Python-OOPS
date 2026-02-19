class Mobile:
    def __init__(self, Brand, Price): 
        self.Brand = Brand
        self.Price = Price

    def display(self):
        print(f"{self.Brand} costs ₹ {self.Price}")

m1 = Mobile("VivoY27",20000)
m2 = Mobile("iphone", 150000)
m1.display()
m2.display()