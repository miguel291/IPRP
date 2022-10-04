def exercicio_3_14(palavra, numero):
    for i in range(len(palavra)-numero+1):
        print(palavra[i:i+numero])

def substitui_vogais_espaco_branco(palavra):
    for i in range (len(palavra)):
        if(palavra[i] == 'a' or palavra[i] == 'e' or palavra[i] == 'i' or palavra[i] == 'o' or palavra[i] == 'u'):
            palavra = palavra[:i] + ' ' + palavra[i+1:]

if __name__ == '__main__':
    exercicio_3_14("Monty Python",3)
    print(substitui_vogais_espaco_branco("Monty Python"))
