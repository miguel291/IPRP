"""Code made in lesson 4 of IPRP course @UniveristyOfCoimbra."""

def ola_mundo():
    """Function that prints "Olá mundo" and then does slicing operations on a wording"""
    print("Olá, \nmundo!")
    wording = "eu sou uma wording yay!"
    print(wording[::2])
    print(max("umqa"))

def replace_vowels_for_blank_space(word):
    """Function that receives a wording a replaces all its vowels by a blank space"""
    new_word = ''
    for i,letter in enumerate(word):
        if word[i] in ('a','e','i','o','u'):
            new_word = new_word + ' '
        else:
            new_word = new_word + word[i]
    print(new_word)

def print_all_subwordings_n_characters(word, n_characters):
    """Receives a word and a integer n and prints out all
    subwordings of the given word with n characters"""
    for i in range(len(word) - n_characters + 1):
        print(word[i : i + n_characters])


def print_all_subwordings_starting_first_character(word):
    """Prints all substrings from string starting in first character"""
    for i in range(len(word) + 1):
        print(word[ : i + 1])

def print_all_subwordings_starting_last_character(word):
    """Receives a wording and prints all its subwordings starting in its last character"""
    for i in range(len(word) + 1):
        print(word[-(i) - 1 : ])

def text_codifier(word, swap_distance):
    """Receives a text and codifies it using the Cesar's Cypher"""
    codified_text = ''
    for i in range(len(word)):
        char = chr(ord(word[i]) + swap_distance)
        if (ord(word[i]) > 64 and ord(word[i]) < 91) | (ord(word[i]) > 96 and ord(word[i]) < 123):
            #print(ord(char),char)
            while ord(char) > 122:
                char = chr(ord(char) - 26)
            while ord(char) < 65 :
                char = chr(ord(char) + 26)
            codified_text = codified_text + char
        else:
            codified_text = codified_text + word[i]
    print(codified_text)

if __name__ == "__main__":
    ola_mundo()
    t1 = (4,5,6,7,8)
    t2 = (1,2,3)
    print("o\nl\ta")
    abc = 1,2,3
    print(abc)
    print(chr(1))
    SOME_STRING = "abcdef"
    SOME_STRING_BACKWARDS = SOME_STRING[::-1]
    print(SOME_STRING_BACKWARDS)
    replace_vowels_for_blank_space("macaco")
    #print_all_subwordings_n_characters('Monty Python', 3)
    #print_all_subwordings_starting_first_character('Monty Python')
    #print_all_subwordings_starting_last_character('Monty Python')
    text_codifier('Monty Python',2)
