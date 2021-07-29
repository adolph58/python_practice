def count_words(filename):
    """计算一个文件大致包含多少单词。"""

    try:
        with open(filename, encoding='utf-8') as f:
            contens = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # 计算该文件大致包含多少个单词。
        words = contens.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
