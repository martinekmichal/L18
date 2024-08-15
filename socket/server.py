import socket
import threading

# Parametre servera
HOST = '127.0.0.1'  # Lokálna adresa
PORT = 12345  # Port, na ktorom server počúva

# Zoznam pripojených klientov
clients = []


def broadcast(message, client_socket):
    """Odošle správu všetkým pripojeným klientom okrem odosielateľa."""
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)


def handle_client(client_socket):
    """Spracováva prichádzajúce správy od klienta."""
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                broadcast(message, client_socket)
            else:
                break
        except:
            break

    client_socket.close()
    clients.remove(client_socket)


def main():
    """Hlavná funkcia na spustenie servera."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(2)
    print("Server beží...")

    while True:
        client_socket, addr = server.accept()
        print(f"{addr} sa pripojil.")
        clients.append(client_socket)
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    main()