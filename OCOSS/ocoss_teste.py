import os
import webbrowser

def iniciar_ocoss():
    print("----- OCOSS iniciado. Digite 'sair' para encerrar ou 'ajuda' para mais informações. -----")
    print("\n🤖 Boas vindas ao OCOSS, o seu mais novo assitente virtual!")
    
    while True:
        comando = input("O que você gostaria de fazer hoje?:").lower().strip()

        if "clima" in comando:
            print("[1] Aplicativo  [2] Navegador  [3] Voltar")
            escolha = input("> ").strip()
            if escolha == "1":
                os.system("start bingweather:")
            elif escolha == "2":
                webbrowser.open("https://www.google.com/search?q=clima+hoje")
            elif escolha == "3":
                print("Voltando...")
                continue
        elif "ajuda" in comando:
            print("""
=== COMANDOS DISPONÍVEIS ===
- clima        Abre a previsão do tempo
- calculadora  Abre a calculadora
 - spotify      Abre o Spotify
- youtube      Abre o YouTube
- ajuda       Mostra esta mensagem
- sair        Encerra o OCOSS
""")

        elif "calculadora" in comando:
            print("Abrindo calculadora...")
            os.system("calc")

        elif "spotify" in comando:
            print("[1] Aplicativo  [2] Navegador  [3] Voltar")
            escolha = input("> ").strip()
            if escolha == "1":
                os.system("start spotify:")
            elif escolha == "2":
                webbrowser.open("https://www.spotify.com")
            elif escolha == "3":
                print("Voltando...")
                continue

        elif "youtube" in comando:
            webbrowser.open("https://www.youtube.com")

        elif "sair" in comando:
            print("Encerrando o OCOSS. Até logo!")
            break

        else:
            print("Comando não reconhecido. Tente: ajuda, clima, calculadora, spotify, youtube.")

iniciar_ocoss()
