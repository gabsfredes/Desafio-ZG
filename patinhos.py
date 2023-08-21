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


patinhos = int(input("Quantos patinhos irão passear? "))
extenso = numeroParaExtenso(patinhos)
print(f'{patinhos} por extenso: {extenso}')

