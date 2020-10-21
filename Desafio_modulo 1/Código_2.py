def funcao_2(num):
    numero_anterior=0
    for i in range(num):
        resultado= numero_anterior + i
        print("Numero A",i,"Numero B", numero_anterior," Resultado: ",resultado)
        lista = list(range(num))

        numero_anterior= i
        print("Essa e a lista",lista)
funcao_2(10)





