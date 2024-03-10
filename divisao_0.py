class ExcDivisaoZero(Exception):
    pass

try:
    num = int(input("Digite um número: "))
    if num == 0:
        raise ExcDivisaoZero("Não é possível dividir por zero!")
    
    resultado = 10 / num
    print(f"A divisão de 10 por {num} é: {resultado}")

except ExcDivisaoZero as e:
    print(e)

except ValueError:
    print("Por favor, digite um número inteiro.")

except Exception as ex:
    print("Erro desconhecido, tente novamente!")