# Выбор аппаратного обеспечения
В качестве сервера будет выступать компьютер.
В качестве датчиков можно использовать:
1. датчик температуры (https://clck.ru/USEud)
2. датчик давления (https://clck.ru/USEvp)

В нашем проекте, с целью экономии, мы использовали компьютеры для имитации датчиков.
# Реализация
Работа выполнялась на языке Python.
# Оценка возможных угроз и разработка действий по их предотвращению
1. отключение датчика
2. отключение сервера
3. атака на сеть

Если происходит отключение датчика, то сервер переходит в режим ожидания до тех пор пока датчик не подключится снова.
Если сервер отключится, то все датчики, подключенные к нему, перейдут в режим ожидания до тех пор пока сервер не возобновит свою работу. 
Наш сервер находится в локальной сети. Атака может произойти в случае плохой защиты. Достаточный уровень защиты можно обеспечить при помощи аутентификации устройств или с помощью других средств. 
# Демонстрация одной из рассмотренных угроз на практике
Отключение датчика - https://imgur.com/a/hugDaL5