def funcao_4(lista_numerica):
    print("valor passado ",lista_numerica)
    a=lista_numerica[0]
    b=lista_numerica[-1]
    if (a==b):
        return True
    else:
        return False
numeros=[10,20,30,40,12,21,10]
print(funcao_4(numeros))

