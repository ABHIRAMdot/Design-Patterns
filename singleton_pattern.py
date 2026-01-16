class AppConfig:
    _instance = None   # store only one object

    def __new__(cls):
        if cls._instance is None:
            print("Creating new object")
            cls._instance = super().__new__(cls)
        return cls._instance


a = AppConfig()
b = AppConfig()

print(a is b)   # True same object
