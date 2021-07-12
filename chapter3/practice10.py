mountains = ['songshan', 'taishan', 'huashan', 'north-hengshan', 'south-hengshan']
mount = ['songshan', 'taishan', 'huashan', 'north-hengshan', 'south-hengshan']

print(mountains)

print(f"中岳：{mountains[0].title()}")

mountains.insert(0, 'huangshan')
print(mountains)

del mountains[0]
print(mountains)

south = mountains.pop()
print(f"删除：{south}")
print(mountains)
east = mountains.pop(1)
print(f"删除：{east}")
print(mountains)

mid = 'songshan'
mountains.remove(mid)
print(f"删除：{mid}")
print(mountains)

mountains.append(south)
mountains.insert(0, mid)
mountains.insert(1, east)
print(mountains)

print("临时排序-正序：sorted()")
print(sorted(mountains))
print("临时排序-负序：sorted(reverse=True)")
print(sorted(mountains, reverse=True))

print("永久排序-正序：sort()")
mountains.sort()
print(mountains)

print("还原列表：")
mountains = list(mount)
print(mountains)

print("永久排序-负序：sort(reverse=True)")
mountains.sort(reverse=True)
print(mountains)

print("还原列表：")
mountains = list(mount)
print(mountains)

print("反转：")
mountains.reverse()
print(mountains)

print("列表长度：")
print(len(mountains))
