variavel = input('Digite alguma coisa: ')

print(f"""
    O tipo primitivo desse valor é: {type(variavel)}
    Só tem espaços? {variavel.isspace()}
    É um número? {variavel.isnumeric()}
    É alfabético? {variavel.isalpha()}
    É alfanumérico? {variavel.isalnum()}
    Está em maiúscula? {variavel.isupper()}
    Está em minúscula? {variavel.islower()}
    Está capitalizada? {variavel.istitle()}
"""
)
