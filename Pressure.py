# test-client.py
import socket
import sys
import time 
import random

# СоздаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаем сокет к порту, через который прослушивается сервер
addr_press = ('localhost', 10001)

while True:
    try:
        sock.connect(addr_press)
        print('Подключено к {} порт {}'.format(*addr_press))
        break
    except:
        print('Нет ответа')
        time.sleep(5)

while True:
    time.sleep(2)
    try:
        # Генерируем и отправляем данные
        
        p_data = 700 + random.randint(-10,30)
        mess = str(int(p_data))
        sock.sendall(mess.encode())
    
        # Проверяем ответ
        sock.recv(1)
    except:
        print('\nОтвет от сервера не получен, попытка переподключения...')
        sock.close()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            try:
                sock.connect(addr_press)
                print('Подключено к {} порт {}'.format(*addr_press))
                break
            except:
                print('Нет ответа')
                time.sleep(5)
        pass