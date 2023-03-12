# Entrada do uduario
string = input("Digite uma palavra para inverter: ")

# Lista vazia para armazenamento
inverted_string = []

for i in range(len(string)-1, -1, -1):
    inverted_string.append(string[i])

inverted_string = ''.join(inverted_string)
print("A string invertida é:", inverted_string)
