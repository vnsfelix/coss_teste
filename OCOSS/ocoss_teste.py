import os
import webbrowser

def iniciar_ocoss():
    print("=== OCOSS iniciado. Digite 'sair' para encerrar. ===")
    
    while True:
        comando = input("\nO que você gostaria de fazer hoje? ").lower().strip()

        if "clima" in comando:
            print("[1] Aplicativo  [2] Navegador  [3] Voltar")
            escolha = input("> ").strip()
            if escolha == "1":
                os.system("start bingweather:")
            elif escolha == "2":
                webbrowser.open("https://www.google.com/search?q=clima+hoje")

        elif "calculadora" in comando:
            print("Abrindo calculadora...")
            os.system("calc")

        elif "spotify" in comando:
            print("[1] Aplicativo  [2] Navegador")
            escolha = input("> ").strip()
            if escolha == "1":
                os.system("start spotify:")
            elif escolha == "2":
                webbrowser.open("https://www.spotify.com")

        elif "youtube" in comando:
            webbrowser.open("https://www.youtube.com")

        elif "sair" in comando:
            print("Encerrando o OCOSS. Até logo!")
            break

        else:
            print("Comando não reconhecido. Tente: clima, calculadora, spotify, youtube.")

iniciar_ocoss()
