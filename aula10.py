"""Code made in class 10 """


def pares_impares(lista):
    """Receives a list of numbers and returns the sum of even numbers and the sum of odd numbers."""
    pares = 0
    impares = 0
    for i in lista:
        if i % 2 == 0:
            pares += i
        else:
            impares += i
    return (pares, impares)


def conta_menores(numero, lista):
    """Receives a number and a list and returns the number of elements in the list that are less than the number."""
    lista.sort()
    count = 0
    for number in lista:
        if number < numero:
            count += 1
        else:
            break
    return count


def soma_cumulativa(lista):
    """Receives a list of numbers and returns a list with the cumulative sum of the numbers."""
    nova_lista = [
        1,
    ]
    for i in range(1, len(lista)):
        nova_lista.append(nova_lista[i - 1] + lista[i])
    return nova_lista


def alterna(lista1, lista2):
    """Receives two lists and returns a list with the elements of the two lists alternating."""
    lista_final = []
    for i in range(len(lista1)):
        lista_final.append(lista1[i])
        lista_final.append(lista2[i])
    return lista_final


if __name__ == "__main__":
    age_list = [12, 18, 20, 25, 30, 40, 50, 60, 70, 80]

    age_list1 = age_list[1:-1]
    for i in range(len(age_list1)):
        print(age_list1[i])

    print("Max age: " + str(max(age_list)))
    print("Max age: " + str(min(age_list)))

    age_total = 0
    for age in age_list:
        age_total += age
    print("Sum all ages: " + str(age_total))

    print(17 in age_list)

    print(pares_impares(age_list))
    print(alterna([1, 2, 3], ["a", "b", "c"]))
    print(conta_menores(20, age_list))
    print(soma_cumulativa([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
