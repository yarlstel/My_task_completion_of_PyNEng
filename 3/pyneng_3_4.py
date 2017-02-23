'''
Задание 3.4

    Из строк command1 и command2 получить список VLAN, которые есть и в команде
    command1 и в команде command2. Не использовать для решения задачи циклы, оператор if.

    command1 = "switchport trunk allowed vlan 1,3,10,20,30,100"
    command2 = "switchport trunk allowed vlan 1,3,100,200,300"
'''

command1 = "switchport trunk allowed vlan 1,3,10,20,30,100"
command2 = "switchport trunk allowed vlan 1,3,100,200,300"

VLANS = set(command1[30:].split(',') + command2[30:].split(','))

print(VLANS)
