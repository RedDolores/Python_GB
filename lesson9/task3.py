class TypedMeta(type):

    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class MyClass(metaclass=TypedMeta):

    def method_1(self):
        pass

    def method_2(self):
        print('!')


obj_1 = MyClass()
obj_2 = MyClass()
obj_3 = MyClass()
print(obj_1 is obj_2)
print(obj_3 is obj_2)
