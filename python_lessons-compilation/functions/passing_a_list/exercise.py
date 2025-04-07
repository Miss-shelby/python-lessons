short_messages=['hello love','i love you','Trust in God','Life is good']

def show_messages(short_msg):
    print("\nFavourite short messages:")
    for msg in short_msg:
        print(msg)

show_messages(short_messages)

# 8-10
def send_messages(short_msgs,sent_mesgs):
    for msg in short_msgs:
        print(f"\nPrinting: {msg}")
        sent_mesgs.append(msg)

sent_messages =[]

send_messages(short_messages[:],sent_messages)
print(short_messages,sent_messages,'original')

# 8_11
send_messages(short_messages[:])