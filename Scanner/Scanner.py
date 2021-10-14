def read_lines(file_name):
    file = open(file_name, 'r')
    Lines = file.readlines()

    count = 0
    for line in Lines:
        count += 1
        print("Line{}: {}".format(count, line.strip()))


def main():
    read_lines('/4308-Project-Fall-2021/Julia-Files/Test1.jl')


main()
