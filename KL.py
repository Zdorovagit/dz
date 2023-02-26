# lst = [1, 2, 3, 4, 5]   iterable object
#
# print(lst.__iter__())
# number_list_iterator = lst.__iter__()   iterator
# print(number_list_iterator)
# print(number_list_iterator.__next__())

# def count_up_to(x):
#     count = 1
#     while count <= x:
#           yield count запоминает текущее состояния
#         count += 1
#
# c = count_up_to(10)
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())

# import datetime
# def raise_to_the_degrees(number, degrees):
#     i = 0
#     for i in range(degrees):
#         yield number ** i
#         i += 1
# res = raise_to_the_degrees(1254853, 500)
# print(res)
# for i in res:
#     print()
#     print(i)

# start = datetime.datetime.now()
# for i in range(500):
#     print(1254853 ** i)
# print(datetime.datetime.now() - start)

# def my_for(iterable):
#     iterator = iterable.__iter__()
#     while True:
#         try:
#             print(iterator.__next__())
#         except StopIteration:
#             break
#
#
# lst = [1, 2, 3, 4, 5]
# my_for(lst)
# for i in lst:
#     print(i, end='')

# def first_func(value):
#     name = value
#
#     def second_func():
#         print('My name is', name)
#
#     return second_func
#
#
# n = first_func('Oleg')
# n()
# a = first_func('Petro')
# a()
# n()

# def count():
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#
#     return inner
#
#
# q = count()
# print(q())
# print(q())
# print(q())
# print(q())
# print(q())
# w = count()
# print(w())
