import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# В отличии от сервера нам тут не нужно биндить, нам тут нужно будет приконектится к серверу
client.connect(('127.0.0.1', 5050)) # Конект к адресу и порту сервера

while True:
    # Тут мы отмечаем сколько информации мы будем получать на один пакет
    data = client.recv(1024)
    print(data.decode('utf-8')) # Выводим и декодируем сообщения
    client.send(input().encode('utf-8')) # Клиентом отправляем на сервер какую то строку

