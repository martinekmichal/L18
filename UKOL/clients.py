import socket
import threading

def prijimej_zpravy(klient_socket):
    while True:
        try:
            zprava = klient_socket.recv(1024).decode()
            if zprava:
                print(zprava)
            else:
                break
        except:
            print("Spojení se serverem bylo ukončeno!")
            break

def main():
    klient_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    klient_socket.connect(('localhost', 5555))

    prijimaci_thread = threading.Thread(target=prijimej_zpravy, args=(klient_socket,))
    prijimaci_thread.start()

    while True:
        zprava = input()
        klient_socket.send(zprava.encode())

main()