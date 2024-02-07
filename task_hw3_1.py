import os
import shutil
import concurrent.futures

def organize_file(file):
    _, extension = os.path.splitext(file)
    if not os.path.exists(extension):
        os.makedirs(extension)
    shutil.move(file, os.path.join(extension, os.path.basename(file)))

def main():
    folder_path = "D:\Uroky\GoIT\WEB\HW_3\hlam"
    files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(organize_file, files)

if __name__ == "__main__":
    main()