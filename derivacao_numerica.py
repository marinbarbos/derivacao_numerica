# x1 = maior valor
# x2 = menor valor
def dois_pontos(fx1, fx2, x1, x2):
    derivada = (fx1-fx2)/(x1-x2)
    return derivada

# x1 = valor a calcular a derivada
# x2 = x com 1 distancia 
# x3 = x com 2 distancias
# progressivo_regressivo = 1-> progressiva, 2-> regressiva
def tres_pontos(f_x1, f_x2, f_x3, x1, x2, x3, progressivo_regressivo = 1):
    if progressivo_regressivo == 1: 
        derivada = ((-3*f_x1)+(4*f_x2)-f_x3)/(x3-x1)
    else: 
        derivada = ((3*f_x1)-(4*f_x2)+f_x3)/(x1-x3)
    return derivada

# MENUS DE INSERÇÃO DE DADOS BEGIN
def dois_progressivo():
    xi = float(input("Favor inserir xi: "))
    xi_mais_1 = float(input("Favor inserir xi+1: "))
    f_xi = float(input("Favor inserir f(xi): "))
    f_xi_mais_1 = float(input("Favor inserir f(xi+1): "))
    print("\nf'(", xi, ") = ", dois_pontos(f_xi_mais_1, f_xi, xi_mais_1, xi), "\n")

def dois_regressivo():
    xi = float(input("Favor inserir xi: "))
    xi_menos_1 = float(input("Favor inserir xi-1: "))
    f_xi = float(input("Favor inserir f(xi): "))
    f_xi_menos_1 = float(input("Favor inserir f(xi-1): "))
    print("\nf'(", xi, ") = ",  dois_pontos(f_xi, f_xi_menos_1, xi, xi_menos_1), "\n")

def dois_central():
    xi_mais_1 = float(input("Favor inserir xi+1: "))
    xi_menos_1 = float(input("Favor inserir xi-1: "))
    f_xi_mais_1 = float(input("Favor inserir f(xi+1): "))
    f_xi_menos_1 = float(input("Favor inserir f(xi-1): "))
    print("\nf'(", xi_mais_1-((xi_mais_1-xi_menos_1)/2), ") = ", dois_pontos(f_xi_mais_1, f_xi_menos_1, xi_mais_1, xi_menos_1), "\n")

def tres_progressivo(user_in):
    xi = float(input("Favor inserir xi: "))
    xi_mais_1 = float(input("Favor inserir xi+1: "))
    xi_mais_2 = float(input("Favor inserir xi+2: "))
    f_xi = float(input("Favor inserir f(xi): "))
    f_xi_mais_1 = float(input("Favor inserir f(xi+1): "))
    f_xi_mais_2 = float(input("Favor inserir f(xi+2): "))
    print("\nf'(", xi, ") = ", tres_pontos(f_xi, f_xi_mais_1, f_xi_mais_2, xi, xi_mais_1, xi_mais_2, user_in), "\n")

def tres_regressivo(user_in):
    xi = float(input("Favor inserir xi: "))
    xi_menos_1 = float(input("Favor inserir xi-1: "))
    xi_menos_2 = float(input("Favor inserir xi-2: "))
    f_xi = float(input("Favor inserir f(xi): "))
    f_xi_menos_1 = float(input("Favor inserir f(xi-1): "))
    f_xi_menos_2 = float(input("Favor inserir f(xi-2): "))
    print("\nf'(", xi, ") = ", tres_pontos(f_xi, f_xi_menos_1, f_xi_menos_2, xi, xi_menos_1, xi_menos_2, user_in), "\n")
# MENUS DE INSERÇÃO DE DADOS END

# MENUS DE SELEÇÃO DE MÉTODO BEGIN 
def menu_dois_pontos():
    print("*********Progressiva, Regressiva ou Central?**********")
    print("1 - Diferença Progressiva")
    print("2 - Diferença Regressiva")
    print("3 - Diferença Central")
    print("0 - Sair")
    print("******************************************************")
    menu_option = int(input())
    if menu_option == 1:
        dois_progressivo()
    elif menu_option == 2:
        dois_regressivo()
    elif menu_option == 3:
        dois_central()

def menu_tres_pontos():
    print("**************Progressiva ou Regressiva?**************")
    print("1 - Diferença Progressiva")
    print("2 - Diferença Regressiva")
    print("0 - Sair")
    print("******************************************************")
    menu_option = int(input())
    if menu_option == 1:
        tres_progressivo(menu_option)
    elif menu_option == 2:
        tres_regressivo(menu_option)
# MENUS DE SELEÇÃO DE MÉTODO END 

def main():
    menu_option = -1
    while menu_option != 0:
        print("********************Quantos Pontos********************")
        print("1 - Dois pontos")
        print("2 - Tres pontos")
        print("0 - Sair")
        print("******************************************************")
        menu_option = int(input())
        if menu_option == 1:
            menu_dois_pontos()
        elif menu_option == 2:
            menu_tres_pontos()  

if __name__ == "__main__":
    main()