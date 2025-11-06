# Soluções:

def sao_anagramas(string1, string2):
  # Todo: Implementar a lógica
  pass

def cifra_de_cesar(texto, deslocamento): 
  # Todo: Implementar a lógica
  pass


def encontrar_maior_palavra(frase: str) -> str:
    maior_palavra = ""
    palavras = frase.split()  # separa palavras por espaços
    for palavra in palavras:
        # remove caracteres não alfanuméricos
        palavra = "".join(filter(str.isalnum, palavra))

        # compara comprimentos
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra
    return maior_palavra
