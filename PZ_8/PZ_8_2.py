#Дан словарь с произвольным количеством элементов. Выяснить имеется ли в нем элемент с ключом «фрукт = яблоко» и если он отсутствует, то добавить его в словарь.
# Вывести на экран первоначальный словарь и измененный.

my_dict = {'name':'Alice','age':35,'city':'New York','fruit':'banana'}
print(my_dict)
if  'fruit' not in my_dict:
    my_dict['fruit'] = 'apple'
    print(my_dict)
else:
    my_dict['fruit'] = 'apple'
    print(my_dict)