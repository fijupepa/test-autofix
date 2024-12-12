string = '123456 67890123 1283791263 127361 12937123 12837 123843'

lista = string.split(" ")
print(lista)

print(f"chunck quantities are {len(lista)}")
print('')
def tamanho_lista(param):
    for pedaco in param:
        if len(pedaco) != 6:
            print(pedaco)

tamanho_lista(lista)