current_users = ['admin', 'John', 'Jack', 'Marry', 'Yilo']
current_users_lower = []

new_users = ['zhangsan', 'lisi', 'JOHN']

for user in current_users:
    current_users_lower.append(user.lower())

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"{user}:该用户名已被使用，请输入别的用户名")
    else:
        print(f"{user}:该用户名未被使用，你可以使用")
