from questionary import Style , questionary
import data
import os
import time

class App:


    def __init__(self):
        self.meses = [
                'Janeiro', 'Fevereiro', 'Março', 'Abril', 
                'Maio', 'Junho', 'Julho', 'Agosto', 
                'Setembro', 'Outubro', 'Novembro', 'Dezembro'
        ]

        self.print = data.Print_Terminal()


    def Menu(self):
        opcoes = ["[1] Adicionar dados",
                    "[2] Mostrar tabela",
                    "[3] Mostrar Rank",
                    "[4] Abrir Log de erros",
                    "[5] Sair"
                ]

        
        custom_style = Style([
            ('highlighted', 'fg:#673ab7 bold'), # opção selecionada
            ('selected', 'fg:#cc5454'),         # opção escolhida
            
        ])

        escolha = questionary.select("Esolha uma opção :",
                                    choices=opcoes,
                                    style=custom_style,
                                    instruction="(utilize as setas)",
                                    ).ask()

        return escolha


    def Voltar_Menu(self,):
        menuresposta = questionary.select(
                    "Deseja voltar ao Menu?",
                    choices=[
                        "Sim",
                        "Não", ]).ask()
        
        return menuresposta

    def Rodar(self,):

        while True:
            escolha = self.Menu()

            if escolha ==   "[2] Mostrar tabela":
                self.print.Print_Tabela()
                menuresp = self.Voltar_Menu()
        
                if menuresp == "Sim":
                    continue
                else:
                    break
            
            elif escolha==  "[3] Mostrar Rank":

                self.print.Print_Rank()
                menuresp = self.Voltar_Menu()
        
                if menuresp == "Sim":
                    continue
                else:
                    break
            
            elif escolha =="[4] Abrir Log de erros":
                self.print.MostrarLog()
                menuresp = self.Voltar_Menu()

                if menuresp == "Sim":
                    continue
                else:
                    break

            elif escolha =="[5] Sair":
                os.system("cls")
                break

app = App()

app.Rodar()
