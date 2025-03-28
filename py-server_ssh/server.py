import socket
import paramiko

# SSH Server Credentials
SSH_HOST = "54.90.86.118"
SSH_PORT = 22
SSH_USER = "ubuntu"
SSH_PASSWORD = "my-ssh-key.pem"

def execute_ssh_command(command):
    """Executes a command on the remote SSH server."""
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(SSH_HOST, port=SSH_PORT, username=SSH_USER, password=SSH_PASSWORD)
        
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()
        
        client.close()
        return output if output else error
    except Exception as e:
        return str(e)

# Server Code
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 22))  # Listen on all interfaces, port 12345
    server_socket.listen(5)
    print("Server listening on port 22...")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection received from {addr}")
        
        command = client_socket.recv(1024).decode()
        print(f"Received command: {command}")
        
        result = execute_ssh_command(command)
        client_socket.send(result.encode())
        client_socket.close()

if __name__ == "__main__":
    start_server()
