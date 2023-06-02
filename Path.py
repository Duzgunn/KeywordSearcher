import os

def search_folder(directory, keyword):

    if not os.path.exists(directory):
        print("Directory does not exist.")
        return
    
    keyword = keyword.lower()

    print("********** Search result in file or directory names **********")
    for path, subdirs, files in os.walk(directory):
        for name in files:
            if keyword in name.lower():
                file_path = os.path.join(path, name)
                print(f"Keyword '{keyword}' was found in {file_path}")

        for dir_name in subdirs:
           if keyword in dir_name.lower():
                dir_path = os.path.join(path, dir_name)
                print(f"Keyword '{keyword}' was found in {dir_path}")


def search_file(directory, keyword):

    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    keyword = keyword.lower()

    print("\n\n********** Search result in files **********")
    for path, subdirs, files in os.walk(directory):
        
        for name in files:
            file_path = os.path.join(path, name)

            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.readlines()
            except UnicodeDecodeError:
                continue

            matches = []
            for i, line in enumerate(content, start=1):
                if keyword in line.lower() or keyword in name.lower():
                    matches.append(i)

            if matches:
                print(f"Keyword '{keyword}' was found in {file_path} on lines: {matches}")

directory = input("Directory path: ")
keyword = input("Keyword: ")

search_folder(directory, keyword)
search_file(directory, keyword)
