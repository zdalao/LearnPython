alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# 获取
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# 插入 Python不关心键 — 值对的添加顺序，而只关心键和值之间的关联关系
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 修改
alien_0['color'] = 'yellow'
print(alien_0)

# 删除
del alien_0['points']
print(alien_0)

user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print('\n')
# keys()里面其实返回了一个列表
for name in favorite_languages.keys():
    print(name.title())

# 遍历字典时，会默认遍历所有的键 缺点 顺序不可测
print('\n')
for name in favorite_languages:
    print(name.title())

print('\n')
# 适用sorted()来获取特定顺序排列
for name in sorted(favorite_languages):
    print(name)

print('\n')
# 字典值打印
for language in favorite_languages.values():
    print(language)

print('\n')

for language in set(favorite_languages.values()):
    print(language)

# 字典列表
# 字典中存储列表
# 字段中存储字典
