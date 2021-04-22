# test-server.py
import socket
import sys

# создаемTCP/IP сокет
sock_press = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_temp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокеты к порту
server_address112 = ('localhost', 10004)
addr_press = ('localhost', 10001)
addr_temp = ('localhost', 10002)
print('Старт сервера на {} порт {}'.format(*addr_press))
print('Старт сервера на {} порт {}'.format(*addr_temp))
sock_press.bind(addr_press)
sock_temp.bind(addr_temp)

# Слушаем входящие подключения
sock_press.listen(1)
sock_temp.listen(1)

while True:
    # ждем подключения всех датчиков
    print('Ожидание подключения всех датчиков...')
    conn_press, press_detect = sock_press.accept()
    conn_temp, temp_detect = sock_temp.accept()
    # пытаемся обработать данные с датчиков
    try:
        print('Датчик температуры подключен:', press_detect)
        print('Датчик давления подключен:', temp_detect)
        # Принимаем данные и отправляем ответ о подключении
        while True: 
           # обработка данных датчика температуры
            try:
                data_temp = conn_temp.recv(8)
                data_temp = float(data_temp.decode())
                data = '1'
                print('Обработка данных датчика температуры')
                print(f'Получено: {data_temp}')
                # проверка температуры
                if data_temp > 35.0:
                    sock_112 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock_112.connect(server_address112)
                    print('\nОтправляем экстренное сообщение о пожаре\n')
                    msg = 'fire'
                    sock_112.sendall(msg.encode())
                    sock_112.close()
                print('Отправка датчику давления пакетов.\n')
                conn_temp.sendall(data.encode())
           # отправка ошибки датчику сервера
            except:
                # отправка ошибки датчику сервера
                conn_press.close()
                conn_temp.close()
                print('Потеряно соединение с датчиком температуры, разрыв соединений...\n')
                break
            # обработка данных датчика давления
            try:
                data_press = conn_press.recv(16)  
                data_press = int(data_press.decode())
                data = '1'
                print('Обработка данных с датчика давления')
                # проверка давления
                if data_press < 700:
                    sock_112 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock_112.connect(server_address112)
                    msg = 'low pressure'
                    print('\nЭкстренное сообщение о низком давлении отправлено\n')
                    sock_112.sendall(msg.encode())
                    sock_112.close()
                print(f'Получено: {data_press}')
                print('Отправка данных датчику давления\n')
                conn_press.sendall(data.encode())
           # отправка ошибки датчику сервера
            except:
                conn_press.close()
                conn_temp.close()
                print('Потеряно соединение с датчиком давления, разрыв соединений...\n')
                break
           # обмен данными с датчиком сервера
    # Ошибка обработки данных, переподключение к датчикам
    except:
        conn_press.close()
        conn_temp.close()
        print('Ошибка обработки данных, переподключение к датчикам...\n')