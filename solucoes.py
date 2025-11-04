# Soluções:

def sao_anagramas(string1, string2):
  count = [0] * 26
  for char in string1:
    if(ord(char) >= ord('a') and ord(char) <= ord('z')):
      count[ord(char) - ord('a')] += 1
    elif(ord(char) >= ord('A') and ord(char) <= ord('Z')):
      count[ord(char) - ord('A')] += 1

  for char in string2:
    if(ord(char) >= ord('a') and ord(char) <= ord('z')):
      count[ord(char) - ord('a')] -= 1
    elif(ord(char) >= ord('A') and ord(char) <= ord('Z')):
      count[ord(char) - ord('A')] -= 1

  for c in count:
    if c != 0:
      return False
  return True

def cifra_de_cesar(texto, deslocamento): 
  # Todo: Implementar a lógica
  pass

def encontrar_maior_palavra(frase):
  # Todo: Implementar a lógica
  pass
