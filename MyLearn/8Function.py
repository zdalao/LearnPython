# 使用def来定义方法
def greet_user():
    print("hello!")


greet_user()


# 默认值只能放最后一个参数
# 请注意，在这个函数的定义中，修改了形参的排列顺序。由于给 animal_type 指定了默认值，
# 无需通过实参来指定动物类型，因此在函数调用中只包含一个实参——宠物的名字。然而，Python
# 依然将这个实参视为位置实参，因此如果函数调用中只包含宠物的名字，这个实参将关联到函数
# 定义中的第一个形参。这就是需要将 pet_name 放在形参列表开头的原因所在。
def describe_pet(animal_type, pet_name='hamster', pet_age=''):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + " 's name is " + pet_name.title() + ".")


# 位置实参
describe_pet('hamster', 'harry')
# 关键字实参
describe_pet(pet_name='harry', animal_type='hamster')


# 方法参数可以传递默认值，列表，可变参使用*标识，传递dict使用**
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k, v in user_info.items():
        profile[k] = v
    return profile


print(build_profile('zheng', 'haomin', age=28, sex="male", dream="do meaningful thing "))
