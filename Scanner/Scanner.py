from collections.abc import Iterable


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
    print(outside_spaces)


def main():
    filepath = '/Users/clyons/Documents/GitHub/Programming_Language_project/4308-Project-Fall-2021/Julia-Files/'
    # filename = input("Enter the name of the file: ")
    filename = 'Test2.jl'

    read_lines(filepath+filename)


main()
