import os


def file_line_amount():
    data = {}
    my_dir = r"C:\Users\乐天\Documents\code\python\regex_"

    for root, dirs, files in os.walk(my_dir):
        for file in files:
            # if file.endswith('.cpp') or file.endswith('.h'):
            # if file.endswith('.java'):
            if file.endswith('.py'):
                file_name = os.path.join(root, file)
                f = open(file_name, 'r', encoding='UTF-8')

                line_amount = 0
                while f.readline() != "":
                    line_amount += 1

                data[file_name] = line_amount

    return data


def print_data(files):
    all_line = 0
    for file_name, line_amount in files.items():
        print(file_name)
        print(line_amount)
        all_line += line_amount
    print()
    print(all_line)


def main():
    files_data = file_line_amount()
    print_data(files_data)


if __name__ == "__main__":
    main()
