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
  pass

def encontrar_maior_palavra(frase):
  # Todo: Implementar a lógica
  pass
