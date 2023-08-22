import inflect
from translate import Translator as MicrosoftTranslator

def traduzir(texto, destino='pt'):
    translator = MicrosoftTranslator(to_lang=destino)
    traducao = translator.translate(texto)
    return traducao

def numeroParaExtenso(patinhos):
    p = inflect.engine()
    extenso = traduzir(p.number_to_words(patinhos))
    return extenso

def convertidoMaiusculo(patinhos):
    converte = numeroParaExtenso(patinhos)
    patinhosExtenso = converte.capitalize()
    return patinhosExtenso

def unidadesPatinhos(patinhos):
    if patinhos == 1:
        unidades = "patinho voltou"
    else: 
        unidades = "patinhos voltaram"   
    return unidades
            
def Letra(patinhos):
    while patinhos >= 1:
        if patinhos > 1:
            return f"{convertidoMaiusculo(patinhos)} patinhos foram passear\nAlém das montanhas\nPara brincar\nA mamãe gritou: Quá, quá, quá, quá\nMas só {convertidoMaiusculo(patinhos-1)} {unidadesPatinhos(patinhos-1)} de lá.\n\n"
        elif patinhos == 1:
            return f"{convertidoMaiusculo(patinhos)} patinho foi passear\nAlém das montanhas\nPara brincar\nA mamãe gritou: Quá, quá, quá, quá\nMas nenhum patinho voltou de lá.\n\n"

def main():
    while True:
        try:
            patinhos = int(input("Quantos patinhos irão passear? "))
            if patinhos >= 1:
                break
            else:
                print("Pelo menos um (1) patinho deve ir passear")
        except ValueError:
            print("Entrada inválida. Deve ser um número inteiro maior ou igual que 1.")

    for patinho in range(patinhos, 0, -1):
        letra = Letra(patinho)
        print(letra)
    
   
if __name__ == "__main__":
    main()