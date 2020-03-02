import random, os

def listGenerator():
    start = random.randint(0, 100)
    end = random.randint(start, 100)

    random_list = list(range(start, end, 2))

    print(random_list)

    return random_list

def binarySearch(_list, value):
    list_len = _list.__len__()

    if list_len == 0:
        return False

    mid = int(list_len / 2)
    if _list[mid] == value:
        return True

    return binarySearch(_list[:mid], value) if value < _list[mid] else binarySearch(_list[mid:], value)

def clearConsole(): os.system('cls' if os.name=='nt' else 'clear')

def inputWithCheck():
    try:
        val = int(input("Digite o valor a pesquisar:\n"))
        clearConsole()
        if val < 0 or val > 100:
            print("Valor deve estar entre 0 e 100!\n\n")
            return -1
        return val
    except ValueError as error:
        print("Valor inválido!\n\n")
        return -1

my_list = listGenerator()
user_input = inputWithCheck()
print("A lista contém o valor " + str(user_input) if binarySearch(my_list, user_input) else "A lista não possui o valor " + str(user_input))