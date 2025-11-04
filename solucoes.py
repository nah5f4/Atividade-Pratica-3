# Soluções:

def sao_anagramas(string1, string2):
  # Todo: Implementar a lógica
  pass

def cifra_de_cesar(texto, deslocamento): 
  # Todo: Implementar a lógica
  #pass
  """
  [A-Z]: [65-90]
  [a-z]: [97-122]
  """
  
  cifra = ""
  for caractere in texto:
    if caractere.isalpha():
      char_val = ord(caractere)
      if char_val < 97:
        cifra += chr((char_val - 65 + deslocamento) % 26 + 65)
      else:
        cifra += chr((char_val - 97 + deslocamento) % 26 + 97)
    else:
      cifra += caractere
  return cifra

def valida_cpf(cpf_string):
  # Todo: Implementar a lógica
  pass
