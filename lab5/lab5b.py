import os

def list_files_in_directory(directory):
    files = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            files.append(file)
    return files

path = input("Введите путь к вложенной папке: ")

folders = path.split("/")
final_folder = folders[-1]
folders = folders[:-1]

print("Путь к папкам:", "/".join(folders))
print("Список файлов в папке", final_folder, ":", list_files_in_directory(path))
