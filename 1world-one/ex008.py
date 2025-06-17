distancia = float(input('Uma distância em metros :'))

print(f'''
A medida de {distancia}m correponde a
{distancia / 1000}km
{distancia / 100}hm
{distancia / 10}dam
{distancia * 0.1}dm
{distancia * 0.01}cm
{distancia * 0.001}mm
''')
