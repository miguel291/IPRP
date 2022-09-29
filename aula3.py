def exercicio_3_14(palavra, numero):
    for i in range(len(palavra)-numero+1):
        print(palavra[i:i+numero])


if __name__ == '__main__':
    exercicio_3_14("Monty Python",3)
