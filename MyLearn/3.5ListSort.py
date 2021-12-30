tourList = ["US", "JP", "CAN", "HK", "THA"]

# 插入
tourList.append("CN")
tourList.insert(0, "UK")
# 删除
del tourList[0]
visit_city = tourList.pop()
print(visit_city)
tourList.remove("CAN")  # 方法 remove() 只删除第一个指定的值

# 修改
tourList[0] = "UK"

for tour in tourList:
    print("i would like to visit " + tour)

print(tourList)
print(sorted(tourList))  # 临时排序
print(sorted(tourList, reverse=True))

# 永久排序
tourList.reverse()
tourList.sort()
tourList.sort(reverse=True)


# 长度
print(len(tourList))
