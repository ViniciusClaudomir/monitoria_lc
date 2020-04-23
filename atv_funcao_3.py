def soma(x,y):
        return x+y

def sub(x,y):
        return x-y

def mult(x,y):
        return x*y

def div(x,y):
        return x/y

while True:
    x = int(input('Informe o valor de X: '))
    y = int(input('Informe o valor de Y: '))
        
    print("Qual operacao voce deseja realizar? [1]-Soma\n[2]-Subtrair\n[3]-Multiplicar\n[4]-Dividir\n[5]-Reiniciar\n[0]- Fechar programa")
    
    escolha = int(input("Digite a opcao: "))
        
    if escolha == 1:
        print(soma(x,y))
        
    elif escolha == 2:
        print(sub(x,y))
        
    elif escolha == 3:
        print(mult(x,y))
        
    elif escolha == 4:
        print(div(x,y))

    elif escolha == 5:
        continue
    else:
            break