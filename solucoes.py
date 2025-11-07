# Soluções:

def sao_anagramas(string1, string2):
  dicionario = {}
  for char in string1:
    if ord(char) == ord(' '):
      continue
    if ord(char) >= ord('A') and ord(char) <= ord('Z'):
      dicionario[ord(char) + 32] = dicionario.get(ord(char) + 32, 0) + 1
    else:
      dicionario[ord(char)] = dicionario.get(ord(char), 0) + 1

  for char in string2:
    if ord(char) == ord(' '):
      continue
    if ord(char) >= ord('A') and ord(char) <= ord('Z'):
      dicionario[ord(char) + 32] = dicionario.get(ord(char) + 32, 0) - 1
    else:
      dicionario[ord(char)] = dicionario.get(ord(char), 0) - 1

  for quantidade in dicionario.values():
    if quantidade != 0:
      return False
  return True

def cifra_de_cesar(texto, deslocamento): 
  # Todo: Implementar a lógica
  #pass
  """
  [A-Z]: [65-90]
  [a-z]: [97-122]
  """
  
  cifra = ""
  for caractere in texto:
    if caractere.isascii() and  caractere.isalpha():  # correção: verifica se é uma letra e se é ascii, preservando os caracteres do texto que não se encaixem aq (incluindo acentuados)
      char_val = ord(caractere)
      if char_val < 97:
        cifra += chr((char_val - 65 + deslocamento) % 26 + 65)
      else:
        cifra += chr((char_val - 97 + deslocamento) % 26 + 97)
    else:
      cifra += caractere
  return cifra


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
