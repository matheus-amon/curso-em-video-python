# #_Exercício_Python_059 = Crie_um_programa_que_leia_dois_valores_e_mostre_um_menu_na_tela:
# #_[_1_]_somar
# #_[_2_]_multiplicar
# #_[_3_]_maior
# #_[_4_]_novos_números
# #_[_5_]_sair_do_programa
# #_Seu_programa_deverá_realizar_a_operação_solicitada_em_cada_caso.

# # %%
# from enum import Enum

# # %%
# class Menu(Enum):
#     somar = 1
#     multiplicar = 2
#     maior = 3
#     novos_números = 4
#     sair_do_programa = 5

# # %%
# class NumberReader:
#     def __init__(self, numbers: list[int], option: int) -> None:
#         self.numbers: list[int] = numbers
#         self.option: int = option
    

# # %%
# print(Menu.maior.name)

# %%
number1 = int(input('Digite um numero: ').strip())
number2 = int(input('Digite outro numero: ').strip())

# %%
OPTIONS = """
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
 """

# %%
while True:
    option: int = int(input(f'Escolha o que quer fazer: \n {OPTIONS} \n -> '))

    if option == 5:
        print('Programa fechado')
        break

    if option == 1:
        result = number1 + number2
        print(result)
    
    if option == 2:
        result = number1 * number2
        print(result)

    if option == 3:
        result = [number1, number2]
        print(max(result))

    if option == 4:
        number1 = int(input('Digite um numero: ').strip())
        number2 = int(input('Digite outro numero: ').strip())
