# test-server.py
import socket
import sys

# создаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# привязываем сокет к порту
addr_112 = ('localhost', 10004)
print('Старт сервера на {} порт {}'.format(*addr_112))
sock.bind(addr_112)

# слушаем входящие подключения
sock.listen(1)

while True:
    # ожидаем соединения
    print('Ожидание соединения...')
    connection, addr_client = sock.accept()
    print('Подключено к:', addr_client)
    data1 = connection.recv(16)
    data1 = data1.decode()
    print(f'Получено: {data1}')
    connection.close()