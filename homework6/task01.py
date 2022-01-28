"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса

Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(some_class):
    class CounterClass(some_class):
        @classmethod
        def init_counter(cls):
            if "count" not in cls.__dict__:
                cls.count = 0

        def __init__(self, *args, **kwargs):
            self.init_counter()
            super().__init__(*args, **kwargs)
            self.__class__.count += 1

        @classmethod
        def get_created_instances(cls) -> int:
            cls.init_counter()
            return cls.count

        @classmethod
        def reset_instances_counter(cls) -> int:
            cls.init_counter()
            temp = cls.count
            cls.count = 0
            return temp

    return CounterClass


@instances_counter
class User:
    """Fodder."""

    pass


# if __name__ == "__main__":
#     print(User.get_created_instances())  # 0
#     user, _, _ = User(), User(), User()
#     print(user.get_created_instances())  # 3
#     print(User.reset_instances_counter())  # 3
#     print(User.reset_instances_counter())  # 0
