# a = int(input("Please enter an integer: "))
# b = int(input("Please enter an integer: "))
# a, b = 0, 1
# # 斐波那契数列
# while b < 10:
#     if b == 8:
#         print(b)
#     else:
#         print(b, end=',')
#     a, b = b, a+b
# words = ['cat', 'window', 'defenestrate']
# for w in range(5):
#     print(w)
#     if w == 2:
#         break
#print(__name__)


class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print_name(self):
        print('%s: %s' % (self.__name, self.__age))

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class StudentChildren(Student):
    pass


print(StudentChildren('seekxy', 21).get_age())
