def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Send message: {current_message}")
        sent_messages.append(current_message)

messages = ['hello', 'haha', 'hihi']
sent_messages = []
send_messages(messages, sent_messages)
print("已发送的消息:")
show_messages(sent_messages)
print("原发送列表:")
show_messages(messages)
