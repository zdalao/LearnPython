magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
print("注意缩进哦~")

# 范围函数 左闭右开
for value in range(1, 5):
    print(value)
# 里用range()来创建列表
numbers = list(range(1, 5))
print(numbers)

print(min(numbers))
print(sum(numbers))
print(max(numbers))

# 神他妈的列表解析
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# practice
# 一行代码完成好多事情
print(sum([value ** 3 for value in range(3, 30, 3)]))

# 切片 左闭右开
print(magicians[0:2])
print(magicians[:2])
print(magicians[1:])
print(magicians[-1:])

# 复制列表 通过切片
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
# not use friend_foods = my_foods

print(my_foods)
print(friend_foods)
friend_foods.append("noodle")
print(friend_foods)
print(my_foods)

# 元组，不可变的列表
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 300  Exception： TypeError: 'tuple' object does not support item assignment
