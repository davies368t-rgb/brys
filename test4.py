class BMW():
    def test(self,fuel_type,max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed

    def test1(self):
        print(self.fuel_type, self.max_speed)

class Ferrari():
    def test(self,fuel_type,max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed

    def test1(self):
        print(self.fuel_type, self.max_speed)

obj1 = BMW()
obj1.test(4,50)
obj1.test1()
obj2 = Ferrari()
obj2.test(4,75)
obj2.test1()