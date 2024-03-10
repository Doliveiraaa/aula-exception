class ExcMaiuscula(Exception):
    pass

def maiuscula_minuscula():
    try:
        texto = input("Digite alguma palavra que tenha ou não letras maiúsculas: ")
        if texto.isupper():
            print("A palavra tem letras maiúscula!")
            
        else:
            raise ExcMaiuscula("A palavra não contém letra maiúscula")

    except ExcMaiuscula as e:
        print(e)

    except ValueError:
        print("Palavra inválida, por favor insira apenas letras.")

    except Exception as ex:
        print("Erro desconhecido, tente novamente.")
