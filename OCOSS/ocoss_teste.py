import os

def iniciar_ocoss():
    while True:
        comando = input("O que o senhor gostaria de fazer hoje? (Ou digite 'sair'): ").lower()

        if "spotify" in comando:
            print("Deseja abir no [1] Aplicativo ou [2] Navegador?")
            escolha = input("> ")