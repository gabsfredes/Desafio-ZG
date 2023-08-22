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

def unidadesPatinhos(patinhos, onde):
    if onde == "letra":
        if patinhos == 1:
            unidades = "patinho voltou"
        else: 
            unidades = "patinhos voltaram"   
    elif onde == "final":
        if patinhos == 1:
            unidades = "o"
        else: 
            unidades = "os"
    
    return unidades
            
def Letra(patinhos):
    while patinhos >= 1:
        unidades = unidadesPatinhos(patinhos-1, "letra")
        if patinhos > 1:
            return f"\n{convertidoMaiusculo(patinhos)} patinhos foram passear\nAlém das montanhas\nPara brincar\nA mamãe gritou: Quá, quá, quá, quá\nMas só {convertidoMaiusculo(patinhos-1)} {unidades} de lá.\n"
        elif patinhos == 1:
            return f"\n{convertidoMaiusculo(patinhos)} patinho foi passear\nAlém das montanhas\nPara brincar\nA mamãe gritou: Quá, quá, quá, quá\nMas nenhum patinho voltou de lá.\n"

def letraFinal(patinhos):
    unidadesUm = unidadesPatinhos(patinhos, "letra")
    unidadesDois = unidadesPatinhos(patinhos, "final")
    return f"Poxa, a mamãe patinha ficou tão triste naquele dia\nAonde será que estavam os seus filhotinhos?\nMas essa história vai ter um final feliz\nSabe por quê?\n\nA mamãe patinha foi procurar\nAlém das montanhas, na beira do mar\nA mamãe gritou: Quá, quá, quá, quá!\nE {unidadesDois} {patinhos} {unidadesUm} de lá\n"

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
        if patinho == 1:
            final = letraFinal(patinhos)
            print(final)
    
   
if __name__ == "__main__":
    main()