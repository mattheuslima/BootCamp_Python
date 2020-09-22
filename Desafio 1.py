print('-='*10)
print('{:=^20}'.format('Desafio 1 - BOOTCAMP'))
print('-='*10)

#idade
idade=int(input('Qual a sua idade:'))
n_id=idade+1
print('No ano que vem você terá {} anos. '.format(n_id))

print('-='*20)
#area do triangulo
lado_a=35
lado_b=14.333333
area=(lado_a)*(lado_b)
print('O retângulo de lado A =%f e lado B = %.2f é %.3f\n'%(lado_a,lado_b,area))

print('-='*20)

#lista

lista_1=[1,2,'IGTI']
lista_2=[2,3,'Bootcamp']
lista_3=lista_1+lista_2 #concatena as listas

print(lista_3)

print('-='*20)

#chute

chute=int(input('Escolha um número entre 0 e 30: '))

adv=[5,6,10,14,16,20,30]

if chute in adv:
    print('Você acertou um dos números que eu pensei. ')
    if chute>15:
        print('\nEsse número é maior que 15')
    if chute<20:
        print('\nEsse número é menor do que 20')

    print('Você é fera')

else:
        print('Que pena, você errou. Tente novamente!\nObrigado por jogar!')

#lista

frutas=["maças","banana","uva","goiaba"]

for x in frutas:
    if x == "uva":
        break
    print(x)


#6

n=5
while n>0:
    n-=1
    print(n)