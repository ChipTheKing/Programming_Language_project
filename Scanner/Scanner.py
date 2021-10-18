
# Class:       CS 4308 Section 02
# Term:        Fall 2021
# Name:       Christopher Lyons
# Instructor:   Sharon Perry
# Project:     Deliverable 1 Scanner


# import statements for program
from collections.abc import Iterable
from Token_dictionary import Tokens  # imports Token dictionary from the token_dictionary.py file
from keyword_dictionary import Keywords  # imports Keyword dictionary from the keyword_dictionary.py file


# function takes in data point and compares it to see if it matches one of the 26 characters in the alphabet
def is_char(file_data):
    # loop runs through all integers from 65 to 122 which represent the english alphabet in the ASCII table
    for x in range(65, 122, 1):
        # checks if the data point is equivalent to the character in the ASCII table
        if file_data == chr(x):
            return True  # returns true if the two values are equivalent
    return False  # returns false if none of the data points are equivalent


# function takes in data point and compares it to see if it matches one of the 10 numbers
def is_int(file_data):
    # loop runs through numbers 0-9 for the number values in the ASCII value
    for x in range(48, 57):
        # checks if the data point is a number 0-9 using ASCII conversion
        if file_data == chr(x):
            return True  # returns true if the two values are equivalent
    return False  # returns false if none of the two data points are equivalent


# function takes in data point and checks to see if it matches a value in the Token dictionary
def is_token(file_data):
    # function call to see if the data point is an int
    if is_int(file_data):
        return True  # if value is an int and returns true if the value is an int
    # function call to see if the data point is a character in the english alphabet
    elif is_char(file_data):
        return True  # returns true if the value is a character in the english alphabet
    # checks if the data point value exists in the Tokens dictionary
    elif file_data in Tokens:
        return True  # returns true if the data point exists in the Tokens dictionary
    else:
        return False  # returns false if the data point doesn't match a value in the Tokens dictionary


# functions takes a data point and returns the matching token from the dictionary if it exists
def set_token(file_data):
    # function call to see if the data point exists as a token
    if is_token(file_data):
        # function call to see if data point is an int so that it can format the right dictionary
        if is_int(file_data):
            return Tokens["int"]  # returns Token value for int from dictionary
        # function call to see if data point is a character so that it can format the right dictionary
        elif is_char(file_data):
            return Tokens["char"]  # returns Token value for char from dictionary
        else:
            return Tokens[file_data]  # returns Token value for data point from dictionary
    else:
        return


# function takes a data point and searches the keyword dictionary to see if it exists in the dictionary
def is_keyword(file_data):
    # checks if the value file_data exists in the dictionary
    if file_data in Keywords:
        return True  # returns true if the value is in the dictionary
    else:
        return False  # returns false if the value is not in the dictionary


# function takes in a nested list and turns it into a single list
def flatten(lis):
    # loops for each item in the list
    for item in lis:
        # checks to see if the item is iterable and is an instance but not a string
        if isinstance(item, Iterable) and not isinstance(item, str):
            # recursive function call
            for x in flatten(item):
                yield x  # yields the x value if the if condition is met
        else:
            yield item  # yields the item if the value if the if condition is not met


# function removes all spaces from the initial list and breaks down the values into single entries
def remove_spaces(lines):
    # variable implementations
    temp = []
    fixed = []
    count = 0
    index = []

    # loop to break down lines into words while removing spaces from between words
    for line in lines:
        temp.append(line.strip())  # uses the strip function to remove exterior spaces from the ends of lines

    # loop to check if the line has a single line comment and removes it if there is
    for x in temp:
        if x[:2] != '//':  # checks if the first 2 values in the line are single comments
            fixed.append(x.split())  # if the line doesn't start with a comment then it breaks the lines into words

    fixed = list(flatten(fixed))  # function call to flatten to turn the nested list into a single list

    # loop to separate values at or inside of parenthesis
    for y in fixed:
        # checks to see if the value ends with (), then separates them into individual values
        if '()' in y:
            # stores the index value for the location in the initial list
            index.append(count)
            value = y[:(len(y ) -2)]  # stores all the characters up to () into a value
            fixed[count] = [value, '(', ')']  # replaces the initial value at the index with the new value and ().

        # if the () have a value inside then it separates them all
        elif '(' in y:
            # stores the index value for the location in the initial list
            index.append(count)
            value = y[:(len(y ) -3)]  # stores values before () into a value
            # stores the value with the separated parenthesis back into list at its former location
            fixed[count] = [value, '(', y[(len(y ) -2)], ')']

        # edge case for if a value has a < attached to it. Separates it and stores it back into the list
        elif '<' in y and len(y) > 1:
            index.append(count)  # index for the value point
            fixed[count] = [y[0], y[1]]  # splits the point into two and saves it at the index

        count += 1  # increases the count index

    fixed = list(flatten(fixed))  # flatten function call again

    return fixed  # returns the fixed list


# function for reading the lines from the given file and storing them into a list
def read_lines(file_name):
    file = open(file_name, 'r')  # opens the file with the note to read only
    lines = file.readlines()  # reads the lines and stores the lines into a list
    outside_spaces = remove_spaces(lines)  # function call to remove all spaces and reformat the list
    return outside_spaces  # returns the list as an output


def main():
    # sets the file past for the file
    filepath = "C:\Dev\Programming_Language_project\\4308-Project-Fall-2021\Julia-Files\\"
    filename = 'Test1.jl'
    # optional input for user to do a file name selection
    # filename = input("Enter the name of the file: ")

    # sets file data list to the output from the function call with the given file
    file_data = read_lines(filepath +filename)

    # prints the outputs in correct formatting
    print("Lexeme\t\t\t\t\tTokens")
    print("---------------------------------------")

    # prints all data points in a formatted stand point using a loop
    for x in file_data:
        # checks if the value is a keyword, token or neither. If neither print error otherwise print dictionary value
        if is_keyword(x):
            print(x, "\t\t\t\t", Keywords[x])
        elif is_token(x):
            print(x, "\t\t\t\t\t", set_token(x))
        else:
            print("Error, unable to calculate at\t", x)


main()
