def validate_user_input(user_input: str) -> str:
    user_input = user_input.upper()

    while user_input not in ['M', 'F']:
        user_input = input('Digite um sexo válido (M/F): ').upper()

    return user_input

user_input: str = str(input('Digite seu sexo (M/F): ').upper().strip())
user_input: str = validate_user_input(user_input=user_input)
print(f'Obrigado! seu sexo é {user_input}')
