class ExcImpar(Exception):
    pass

try:
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        print("O número é PAR!")

    else:
        raise ExcImpar ("O número IMPAR não pode ser informado!")
    
except ExcImpar as e:
    print(e)

except ValueError:
    print("valor informado não é um inteiro!")

except Exception:
    print("Erro desconhecido, tente novamente:")