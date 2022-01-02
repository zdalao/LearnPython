# 一些判断
age = 28
print(age == 28)
print(age > 28)
print(age < 28)
print(age >= 28)
print(age <= 28)

print(age != 28)
print(age > 28 and age < 56)
print(age > 28 or age < 0)
ages = [28, 29, 30]
print(age in ages)
print(age not in ages)

can_edit = True
print(can_edit)

if age > 18:
    print("You are old enough to vote!")
    print("Have you registered to yet?")
elif age > 16:
    print("Good")
else:
    print("Sorry,you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# 确定列表不是空的
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making you pizza!")
else:
    print("Are you sure to want a plan pizza?")




