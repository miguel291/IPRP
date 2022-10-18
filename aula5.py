"""Code made in lesson 5 of IPRP course @UniveristyOfCoimbra."""


def return_largest_3_numbers(number1, number2, number3):
    """Receives 3 integers and returns the largest"""
    largest = 0
    if number1 > number2:
        largest = number1
    else:
        largest = number2
    if number3 > largest:
        return number3
    return largest


def print_dumb_table_with_n_rows(rows):
    """Prints a table with a number and its square"""
    print("Número\tQuadrado")
    for i in range(rows):
        print(f"{i+1:6d}\t{(i+2)**2:8d}")
        # print("{0}\t{1}".format(i+1,(i+1)**2))


def miles_to_kilometer_converter(rows):
    """Converts miles to kilometers"""
    print("Milhas\tQuilometros")
    for i in range(rows):
        j = (float)(i)
        print(f"{j+1:6.2f}\t{(j+1)*1.609:10.2f}")


def tabuada(numero):
    """Prints the tabuada of a given number"""
    print(f"Tabuada do numero {numero}\n-------------------")
    for i in range(1, 11):
        print(f"{numero}\tX\t{i}\t=\t{numero*i}")


def acronym_builder(name):
    """Builds the acronym of the name given"""
    words = name.split(" ")
    acronym = ""
    for word in words:
        acronym += word[0]
    return acronym


if __name__ == "__main__":
    print(return_largest_3_numbers(9, 4, 7))
    print_dumb_table_with_n_rows(5)
    miles_to_kilometer_converter(5)
    tabuada(7)
    print(acronym_builder("Random Access Memory"))
