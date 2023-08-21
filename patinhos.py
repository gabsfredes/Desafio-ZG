import inflect
from googletrans import Translator

def traduzir(texto, destino='pt'):
    translator = Translator()
    traducao = translator.translate(texto, dest=destino)
    return traducao.text

def numeroParaExtenso(patinhos):
    p = inflect.engine()
    extenso = traduzir(p.number_to_words(patinhos))
    return extenso

def main():
    while True:
        try:
            patinhos = int(input("Quantos patinhos irão passear? "))
            if patinhos > 1:
                break
            else:
                print("Pelo menos um (1) patinho deve ir passear")
        except ValueError:
            print("Entrada inválida. Deve ser um número inteiro maior ou igual que 1.")

    patinhosExtenso = numeroParaExtenso(patinhos)

    print(f'{patinhosExtenso} irão passear')

if __name__ == "__main__":
    main()