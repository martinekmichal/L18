import socket
import threading

# Parametre klienta
HOST = '127.0.0.1'  # Adresa servera
PORT = 12345  # Port, na ktorom server počúva


def receive_messages(client_socket):
    """Prijíma správy od servera."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except:
            break


def main():
    """Hlavná funkcia na spustenie klienta."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    print("Pripojený k serveru. Môžete začať chatovať.")

    name = input("Zadaj tvoje chatove meno: ")

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        client_socket.send(f"{name}: {message}".encode('utf-8'))


if __name__ == "__main__":
    main()