class ExcImpar(Exception):
    pass

try:
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        print("O número é PAR!")

    else:
        raise ExcImpar ("O número IMPAR não pode ser informado!")
    
#tratar erro que o número é impar
except ExcImpar as e:
    print(e)

#tratar erro ValueError
except ValueError:
    print("valor informado não é um inteiro!")

#tratar qualquer erros
except Exception:
    print("Erro desconhecido, tente novamente:")