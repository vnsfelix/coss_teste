import os

def iniciar_ocoss():
    while True:
        comando = input("\nO que o senhor gostaria de fazer hoje? (Ou digite 'sair'): ").lower().strip()

        if "calculadora" in comando:
            print("Deseja abir o [1] Aplicativo? ou [2] para sair")
            escolha = input("> ")

            if escolha == "1":
                print("Abrindo calculadora...")
                os.system("start Calculadora")
            else:
                print("opção invalida.")
        elif escolha == "2":
            print("Finalizando Sistema...")
            break
        else:
            print("Desculpe, não reconheço esse comando.")

        if "spotify" in comando:
            print("Deseja abir no [1] Aplicativo ou [2] Navegador?")
            escolha = input("> ")

            if escolha == "1":
                print("Abrindo spotify...")
                os.system("start spotify")
            elif escolha == "2":
                print("Abrindo Navegador...")
                os.system("start https://www.spotify.com")
            else:
                print("opção invalida.")
        elif "sair" in comando:
            print("Finalizando Sistema...")
            break
        else:
            print("Desculpe, não reconheço esse comando.")
        
iniciar_ocoss()
