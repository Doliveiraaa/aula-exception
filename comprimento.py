class ExcComprimentoDiferente(Exception):
    pass

try:
    string1 = input("Digite a primeira palavra: ")
    string2 = input("Digite a segunda palavra: ")
    
    if len(string1) != len(string2):
        raise ExcComprimentoDiferente("As palavras tem tamanhos diferentes.")

    print("As palavras tem o mesmo comprimento!")

except ExcComprimentoDiferente as e:
    print(e)

except ValueError:
    print("Erro! Por favor, insira apenas textos.")

except Exception as ex:
    print("Erro desconhecido, tente novamente!")