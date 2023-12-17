#Приведенный выше код удалит файл file3.txt в текущей рабочей папке.

if __name__ == "__main__":
    import os

    # deleting the file named file3.txt
    os.remove("file3.txt")