def show_messages(msgs):
    print("showing all messages: ")
    for msg in msgs:
        print(msg)

def send_messages(msgs):
    """Print each message, and then move it to sent_messages."""
    print("\nsending all messages: ")
    while msgs:
        current_msg = msgs.pop()
        print(current_msg)
        sent_msgs.append(current_msg)

msgs = ["good morning", "hi", "how are you?", "better now we're talking :)"]
show_messages(msgs)

sent_msgs = []
send_messages(msgs[:])

print("\nFinal list:")
print(msgs)
print(sent_msgs)


