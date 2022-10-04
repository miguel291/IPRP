def ola_mundo():
    print("Olá, \nmundo!")
    string = "eu sou uma string yay!"
    print(string[::2])
    print(max("umqa"))

def replace_vowels_for_blank_space(word):
    new_word = ''
    for i in range(len(word)):
        if(word[i] in ('a','e','i','o','u')):
            new_word = new_word + ' '
        else:
            new_word = new_word + word[i]
    print(new_word)

def print_all_substrings_n_characters(str, n_characters):
    for i in range(len(str) - n_characters + 1):
        print(str[i : i + n_characters])


def print_all_substrings_starting_first_character(str):
    for i in range(len(str) + 1):
        print(str[ : i + 1])

def print_all_substrings_starting_last_character(str):
    for i in range(len(str) + 1):
        print(str[-(i) - 1 : ])
    
def text_codifier(str, swap_distance):
    codified_text = ''
    for i in range(len(str)):
        char = chr(ord(str[i]) + swap_distance)
        if((ord(str[i]) > 64 and ord(str[i]) < 91) | (ord(str[i]) > 96 and ord(str[i]) < 123)):
            #print(ord(char),char)
            while(ord(char) > 122):
                char = chr(ord(char) - 26)
            while(ord(char) < 65):
                char = chr(ord(char) + 26)
            codified_text = codified_text + char
        else:
            codified_text = codified_text + str[i]
    print(codified_text)

if __name__ == "__main__":
    """ola_mundo()
    t1 = (4,5,6,7,8)
    t2 = (1,2,3)
    print("o\nl\ta")
    abc = 1,2,3,
    print(abc)
    print(chr(1))
    string = "abcdef"
    s = string[::-1]
    print(s)"""
    #replace_vowels_for_blank_space("macaco")
    #print_all_substrings_n_characters('Monty Python', 3)
    #print_all_substrings_starting_first_character('Monty Python')
    #print_all_substrings_starting_last_character('Monty Python')
    text_codifier('Monty Python',2)

