"""
你还可以导入模块中的特定函数，这种导入方法的语法如下：
from module_name import function_name
通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：
from module_name import function_0 , function_1 , function_2
"""

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
