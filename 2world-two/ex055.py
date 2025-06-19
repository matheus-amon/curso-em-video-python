weights: list = [] 
for p in range(1, 6):
    weight = input(f'peso da {p}º pessoa: ')
    weight: float = float(weight)
    
    weights.append(weight)
    
print(f'''
maior: {max(weights)}
menor: {min(weights)}
''')
