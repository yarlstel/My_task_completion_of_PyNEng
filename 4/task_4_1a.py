"""
Задание 4.1a

Всё, как в задании 4.1. Но, если пользователь ввел адрес хоста, а не адрес сети,
то надо адрес хоста преобразовать в адрес сети и вывести адрес сети и маску, как в задании 4.1.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.
"""

from ipaddress import ip_interface

def print_network(_network):
    '''
    Печатает сеть в десятичном и двоичном форматах
    '''
    network_splited = str(_network).split('.')
    for i in network_splited:
        print('{:10}'.format(i), end='')
    print('')
    for i in network_splited:
        print('{:10}'.format('0' * (8 - len(bin(int(i))[2:])) + bin(int(i))[2:]), end='')
    print('')



try:
    ip_address = ip_interface(input('Введите сеть в формате: 10.1.1.0/24: '))
except ValueError:
    print("Не удалось распознать сеть.")
    exit()

if ip_address.version == 6:
    print("Скрипт не рассчитан на работу с IPv6")
    exit()

print_network(ip_address.network.network_address)

print('\nMask:\n{}'.format(ip_address.network.prefixlen))
print_network(ip_address.network.netmask)

