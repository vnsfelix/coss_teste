import os

def iniciar_ocoss():
    while True:
        comando = input("\nO que o senhor gostaria de fazer hoje? (Ou digite 'sair'): ").lower()

        if "spotify" in comando:
            print("Deseja abir no [1] Aplicativo ou [2] Navegador?")
            escolha = input("> ")

            if escolha == "1":
                os.system("start spotify")
            elif escolha == "2":
                os.system("start https://www.spotify.com")
            else:
                print("opção invalida.")
        elif "sair" in comando:
            print("Finalizando Sistema...")
            break
        else:
            print("Desculpe, não reconheço esse comando.")
        
iniciar_ocoss()
