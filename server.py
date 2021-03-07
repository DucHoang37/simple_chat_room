import socket
import threading
host = '127.0.0.1'
port = 12345
# Chạy Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Danh sách người dùng và nickname
users = []
nicknames = []

# Gửi tin nhắn cho tất cả các user đã kết nối vào chatroom
def broadcast(message):
    for user in users:
        user.send(message)

# Xử lý tin nhắn từ user
def xu_ly(user):
    while True:
        try:
            # Truyền tin nhắn
            message = user.recv(1024)
            broadcast(message)
        except:
            # User rời khỏi chatroom
            index = users.index(user)
            users.remove(user)
            user.close()
            nickname = nicknames[index]
            broadcast('{} đã rời phòng chat!'.format(nickname).encode("utf-8"))
            nicknames.remove(nickname)
            break

# Hàm nghe và nhận
def receive():
    while True:
        # Chấp nhận kết nối
        user, address = server.accept()
        print(">>> Kết nối với {}".format(str(address)))

        # Request And Store Nickname
        user.send("nick".encode("utf-8"))
        nickname = user.recv(1024).decode("utf-8")
        nicknames.append(nickname)
        users.append(user)

        # Print And Broadcast Nickname
        print(">>> Nickname is {}".format(nickname))
        broadcast("{} đã tham gia phòng chat!".format(nickname).encode("utf-8"))
        user.send("Kết nối với server!".encode("utf-8"))

        # Start Handling Thread For Client
        thread = threading.Thread(target=xu_ly, args=(user,))
        thread.start()

receive()