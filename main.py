# Используя подготовленную строку nat, получить новую строку, в которой в
# имени интерфейса вместо FastEthernet написано GigabitEthernet.
# Полученную новую строку вывести на стандартный поток вывода (stdout) с
# помощью print.#
# Ограничение: Все задания надо выполнять используя только пройденные темы.#
# nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
target = 'FastEthernet0/1'
replacement = 'GigabitEthernet'

print(nat.replace(target, replacement))
