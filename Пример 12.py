#Приведенный код выведет имя текущего рабочего каталога.

if __name__ == "__main__":
    import os

    path = os.getcwd()
    print(path)