import socket

SERVER_IP = "54.90.86.118"  # Change to your server's IP
SERVER_PORT = 22

def send_command(command):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    client_socket.send(command.encode())

    response = client_socket.recv(4096).decode()
    print("Server Response:\n", response)
    client_socket.close()

if __name__ == "__main__":
    while True:
        cmd = input("Enter command to execute on SSH server: ")
        if cmd.lower() == "exit":
            break
        send_command(cmd)
