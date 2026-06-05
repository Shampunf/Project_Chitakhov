#Создать словарь my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}.
#Добавьте пару 'profession': 'Doctor', измените age на 40 и выведите значение city.

my_dict = {'name':'Alice','age':35,'city':'New York'}
print(my_dict)
my_dict.update({'age':40,"profession": "Doctor"})
print(my_dict)
print(my_dict['city'])