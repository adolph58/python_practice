alien_0 = {'color': 'green', 'points':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {'color': 'green'}
print(f"The alien is {alien_1['color']}")

alien_1['color'] = 'yellow'
print(f"The alien is now {alien_1['color']}")

alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original positon: {alien_0['x_position']}")

alien_2['speed'] = 'fast'

# 向右移动外星人。
# 根据当前速度确定将外星人向右移动多远。
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的移动速度肯定很快。
    x_increment = 3

# 新位置为旧位置加上移动距离。
alien_2['x_position'] = alien_2['x_position'] + x_increment

print(f"New position: {alien_2['x_position']}")
