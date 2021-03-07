import socket
import threading

print("""
	█▀ █ █▀▄▀█ █▀█ █   █▀▀   █▀▀ █ █ ▄▀█ ▀█▀   █▀█ █▀█ █▀█ █▀▄▀█
	▄█ █ █ ▀ █ █▀▀ █▄▄ ██▄   █▄▄ █▀█ █▀█  █    █▀▄ █▄█ █▄█ █ ▀ █
""")

# Tạo username (tùy thích, có thể có dấu tiếng Việt)
nickname = input(">>> Tạo username: ")

# Kết nối đến Server
user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user.connect(('127.0.0.1', 12345))

def receive():
    while True:
        try:
            # Nhận tin nhắn từ Server
            message = user.recv(1024).decode("utf-8")
            if message == 'nick':
                user.send(nickname.encode("utf-8"))
            else:
                print(f">>> {message}")
        except:
            # Đóng kết nối khi có lỗi
            print(">>> Lỗi!!")
            user.close()
            break

# Gửi tin nhắn đến Server
def write():
    while True:
        message = "{}: {}".format(nickname, input(""))
        user.send(message.encode('utf-8'))




# Bắt đầu "lắng nghe" và viết tin nhắn
receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()