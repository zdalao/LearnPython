# 根据约定，在Python中，首字母大写的名称指的是类。
# 这个类定义中的括号是空的，因为我们要从空白创建这个类
class Dog():
    """一次模拟小狗的简单尝试"""

    #  __init__() 是一个特殊的方法，每当你根据 Dog 类创建新实
    # 例时，Python都会自动运行它。在这个方法的名称中，开头和末尾各有两个下划线，这是一种约
    # 定，旨在避免Python默认方法与普通方法发生名称冲突。
    #  self ，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " roller over!")


my_dog = Dog('white', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + "year's old")

my_dog.sit()
my_dog.roll_over()
