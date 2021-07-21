favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

users = ['jen', 'sarah', 'edward',  'phil', 'jack', 'mary']

for user in users:
    if user in favorite_languages.keys():
        print(f"{user.title()}, thank you involve in the investigation")
    else:
        print(f"{user.title()}, we want you to invole in the investigation")
