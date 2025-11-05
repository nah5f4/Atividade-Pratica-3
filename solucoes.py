# Soluções:

def sao_anagramas(string1, string2):
  # Todo: Implementar a lógica
  pass

def cifra_de_cesar(texto, deslocamento): 
  # Todo: Implementar a lógica
  pass


def encontrar_maior_palavra(frase: str) -> str:
    maio_palavra = ""
    frase_sem_pontuacao = ""
    for caractere in frase:
        if (caractere.lower() >= "a" and caractere.lower() <= "z") or caractere == " ":
            frase_sem_pontuacao += caractere  # ignora caracteres que não são letras

    palavras = frase_sem_pontuacao.split()  # separa palavras por espaços
    for palavra in palavras:
        if len(palavra) > len(maio_palavra):
            maio_palavra = palavra
    return maio_palavra
