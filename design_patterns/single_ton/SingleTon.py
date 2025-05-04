# method - 1
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton , cls).__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 == s2)


# method - 2

