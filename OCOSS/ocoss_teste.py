import os

def iniciar_ocoss():
    while True:
        comando = input("\nO que o senhor gostaria de fazer hoje? (Ou digite 'sair'): ").lower().strip()

        if "clima" in comando:
            print("Deseja abir no [1] Aplicativo ou [2] Navegador? | Digite [3] para voltar")
            escolha = input("> ")

            if escolha == "1":
                print("Abrindo Previsão do Tempo...")
                os.system("start bingweather:")
                
            elif escolha == "2":
                print("Abrindo Navegador")
                os.system("start https://www.google.com/search?q=google+clima&sca_esv=09c971a9c1a6e973&biw=1920&bih=945&sxsrf=ANbL-n7cpq_tZ9DNPy_0SitfpngNnj761g%3A1777471634152&ei=khDyafGFCdCf5OUP2OujqQ4&oq=goo&gs_lp=Egxnd3Mtd2l6LXNlcnAiA2dvbyoCCAEyFhAuGIAEGIoFGEMYsQMYgwEYxwEY0QMyChAAGIAEGIoFGEMyChAAGIAEGIoFGEMyDRAAGIAEGIoFGEMYsQMyCxAAGIAEGLEDGIMBMhAQABiABBiKBRhDGLEDGIMBMggQABiABBixAzIQEAAYgAQYigUYQxixAxiDATINEAAYgAQYigUYQxixAzILEAAYgAQYsQMYgwEyJRAuGIAEGIoFGEMYsQMYgwEYxwEY0QMYlwUY3AQY3gQY4ATYAQJIjhdQ7wNY3w5wAngBkAEDmAFxoAHnCqoBBDIuMTG4AQPIAQD4AQGYAgagAqsDqAIUwgIKEAAYRxjWBBiwA8ICDRAAGIAEGIoFGEMYsAPCAhcQLhjYAhi4BhjaBhjcBhjIAxiwA9gBAcICFxAuGNwGGLgGGNoGGNgCGMgDGLAD2AEBwgIQEAAYgAQYigUYQxixAxjJA8ICCxAAGIAEGLEDGJIDwgILEAAYgAQYigUYkgPCAgcQABiABBgKwgIFEAAYgATCAhYQABiABBiKBRhDGOcGGOoCGLQC2AEBwgIcEC4YgAQYigUYQxjnBhjHARjRAxjqAhi0AtgBAcICEBAAGAMYjwEY6gIYtALYAQLCAhAQLhgDGI8BGOoCGLQC2AECwgIREC4YgAQYsQMYgwEYxwEY0QPCAhMQLhiABBiKBRhDGLEDGMcBGNEDmAME8QVVAT6-PZhd6ogGAZAGDboGBAgBGBm6BgYIAhABGAqSBwMyLjSgB8ZPsgcDMC40uAejA8IHBTAuMy4zyAcRgAgB&sclient=gws-wiz-serp")
            elif escolha == "3":
                print("Voltando...")
                continue
            else:
                print("opção invalida.")
        elif "sair" in comando:
            print("Finalizando Sistema...")
            break
        else:
            print("Desculpe, não reconheço esse comando.")

        if "calculadora" in comando:
            print("Deseja abir no [1] Aplicativo ou [2] voltar?")
            escolha = input("> ")

            if escolha == "1":
                print("Abrindo calculadora...")
                os.system("calc")
            elif escolha == "2":
                print("Voltando...")
                continue
            else:
                print("opção invalida.")
        elif "sair" in comando:
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
