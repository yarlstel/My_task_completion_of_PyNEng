'''
Задание 7.1

Создать функцию, которая генерирует конфигурацию для access-портов.

Параметр access ожидает, как аргумент, словарь access-портов, вида:
    { 'FastEthernet0/12':10,
      'FastEthernet0/14':11,
      'FastEthernet0/16':17,
      'FastEthernet0/17':150 }

Функция должна возвращать список всех портов в режиме access
с конфигурацией на основе шаблона access_template.

В конце строк в списке не должно быть символа перевода строки.

Проверить работу функции на примере словаря access_dict.
'''

def generate_access_config(access):
    """
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17}

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']
    result = []
    for intf in access:
        result.append('interface {}'.format(intf))
        for line in access_template:
            if line.endswith('vlan'):
                result.append('{} {}'.format(line, access[intf]))
            else:
                result.append(line)
    return result


access_dict = {'FastEthernet0/12':10,
               'FastEthernet0/14':11,
               'FastEthernet0/16':17,
               'FastEthernet0/17':150}
print(generate_access_config(access_dict))
