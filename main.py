import os


def file_line_amount(dir_name, file_postfix):
    data = {}

    for root, dirs, files in os.walk(dir_name):
        for file in files:
            if file.endswith(file_postfix):
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
    dir_name = r"C:\Users\乐天\Documents\code\python\regex_"
    file_postfix = ".py"
    files_data = file_line_amount(dir_name, file_postfix)
    print_data(files_data)


if __name__ == "__main__":
    main()
