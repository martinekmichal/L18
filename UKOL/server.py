import socket
import threading

uzivatele = {
    "uzivatel1": "heslo1",
    "uzivatel2": "heslo2",
}
klienti = []

def broadcast(zprava, klient_socket):
    for klient in klienti:
        if klient != klient_socket:
            try:
                klient.send(zprava)
            except:
                klienti.remove(klient)

def obsluhuj_klienta(klient_socket, klient_adresa):
    try:
        klient_socket.send('b"Zadej své uživateksé jméno: "')
        uzivatelske_jmeno = klient_socket.recv(1024).decode().strip()

        klient_socket.send('b"Zadej heslo: "')
        heslo = klient_socket.recv(1024).decode().strip()

        if uzivatele.get(uzivatelske_jmeno) == heslo:
            klient_socket.send('b"Přihlášení úspěšné! Vítej!.\n"')
            broadcast(f"{uzivatelske_jmeno} se připojil/a k chatu.\n".encode(), klient_socket)
            klienti.append(klient_socket)

        while True:
            zprava = klient_socket.recv(1024)
            if not zprava:
                break
            broadcast(f"{uzivatelske_jmeno}: {zprava.decode()}".encode(), klient_socket)

        else:
            klient_socket.send('b"Neplatné uživatelské jméno nebo heslo. Odpojeno!!.\n"')
            klient_socket.close()

    except Exception as e:
        print(f"Chyba je: {e}")
        klient_socket.close()

    finally:
        if klient_socket in klienti:
            klient.remove(klient_socket)
            broadcast(f"{uzivatelske_jmeno} se odpojil/a z chatu.\n".encode(), klient_socket)

def spust_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 5555))
    server_socket.listen(5)
    print("Server běží a čeká na připojení...")

    while True:
        klient_socket, klient_adresa = server_socket.accept()
        print(f"Připojen nový klient: {klient_adresa}")
        thread = threading.Thread(target=obsluhuj_klienta, args=(klient_socket, klient_adresa))
        thread.start()

spust_server()
