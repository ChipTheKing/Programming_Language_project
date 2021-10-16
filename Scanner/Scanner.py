from collections.abc import Iterable
from Token_dictionary import Tokens
from keyword_dictionary import Keywords


def is_char(file_data):
    for x in range(65, 122, 1):
        if file_data == chr(x):
            return True
    return False


def is_int(file_data):
    for x in range(48, 57):
        if file_data == chr(x):
            return True
    return False


def is_token(file_data):
    if is_int(file_data):
        return True
    elif is_char(file_data):
        return True
    elif file_data in Tokens:
        return True
    else:
        return False


def set_token(file_data):
    if is_token(file_data):
        if is_int(file_data):
            return Tokens["int"]
        elif is_char(file_data):
            return Tokens["char"]
        else:
            return Tokens[file_data]
    else:
        return


def is_keyword(file_data):
    if file_data in Keywords:
        return True
    else:
        return False


#
def flatten(lis):
    for item in lis:
        if isinstance(item, Iterable) and not isinstance(item, str):
            for x in flatten(item):
                yield x
        else:
            yield item


#
def remove_spaces(lines):
    temp = []
    fixed = []
    count = 0
    index = []

    for line in lines:
        temp.append(line.strip())

    for x in temp:
        if x[:2] != '//':
            fixed.append(x.split())

    fixed = list(flatten(fixed))

    for y in fixed:
        if '()' in y:
            index.append(count)
            value = y[:(len(y)-2)]
            fixed[count] = [value, '(', ')']

        elif '(' in y:
            index.append(count)
            value = y[:(len(y)-3)]
            fixed[count] = [value, '(', y[(len(y)-2)], ')']

        elif '<' in y and len(y) > 1:
            index.append(count)
            fixed[count] = [y[0], y[1]]

        count += 1

    fixed = list(flatten(fixed))

    return fixed


# function for reading the lines from the given file and storing them into a list
def read_lines(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    outside_spaces = remove_spaces(lines)
    return outside_spaces


def main():
    filepath = '/Users/clyons/Documents/GitHub/Programming_Language_project/4308-Project-Fall-2021/Julia-Files/'
    # filename = input("Enter the name of the file: ")
    filename = 'Test3.jl'

    file_data = read_lines(filepath+filename)

    print("Lexeme", "                   ", "Tokens")
    print("---------------------------------------")

    for x in file_data:
        if is_keyword(x):
            print(x, "                 ", Keywords[x])
        elif is_token(x):
            print(x, "                 ", set_token(x))
        else:
            print("Error, unable to calculate at ", x)


main()
