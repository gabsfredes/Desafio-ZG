import inflect

def numero_para_extenso(numero):
    p = inflect.engine()
    extenso = p.number_to_words(numero)
    return extenso

numero = int(input("Digite um número: "))
extenso = numero_para_extenso(numero)
print(f'{numero} por extenso: {extenso}')