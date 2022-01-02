class Car():
    def __init__(self, make, model, year):
        """
        初始化描述汽车的属性
        @param make:
        @param model:
        @param year:
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_new_car = Car("audi", 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 修改属性值
# 直接通过实例进行修改；
# 通过方法进行设置；
# 通过方法进行递增（增加特定的值）

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(24)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()


# 继承 一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；原有的类称为父类，
# 而新类称为子类。子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。
class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


# 对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写。为此，可在子
# 类中定义一个这样的方法，即它与要重写的父类方法同名。这样，Python将不会考虑这个父类方
# 法，而只关注你在子类中定义的相应方法

# 类中的属性可以使用别的类来更好的抽象
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on full charge"
        print(message)


class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()