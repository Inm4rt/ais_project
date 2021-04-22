# test-client.py
import socket
import sys
import time 
import random

# СоздаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаем сокет к порту, через который прослушивается сервер
addr_temp = ('localhost', 10002)

while True:
            try:
                sock.connect(addr_temp)
                print('Подключено к {} порт {}'.format(*addr_temp))
                break
            except:
                print('Нет ответа')
                time.sleep(5)

while True:
    time.sleep(2)
    try:
        # Генерируем и отправляем данные
        data_temp = random.randint(-5,50)
        data_temp = round(data_temp, 2)
        msg = str(data_temp)
        sock.sendall(msg.encode())
    
        # Проверяем ответ
        sock.recv(1)
    except:
        print('\nОтвет от сервера не получен, попытка переподключения...')
        sock.close()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            try:
                sock.connect(addr_temp)
                print('Подключено к {} порт {}'.format(*addr_temp))
                break
            except:
                print('Нет ответа')
                time.sleep(5)
        pass

