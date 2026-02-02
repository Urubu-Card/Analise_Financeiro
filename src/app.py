from questionary import Style , questionary
import data

class App:


    def __init__(self):
        self.meses = [
                'Janeiro', 'Fevereiro', 'Março', 'Abril', 
                'Maio', 'Junho', 'Julho', 'Agosto', 
                'Setembro', 'Outubro', 'Novembro', 'Dezembro'
        ]

        self.busca = data.Busca()

    def Menu(self):
        opcoes = ["[1] Adicionar dados",
                    "[2] Mostrar tabela",
                    "[3] Mostrar Rank",""
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

    def Rodar(self,):

        while True:
            escolha = self.Menu()



            if escolha == "[2] Mostrar tabela":

                self.busca.Tabela()
                menures = questionary.select(
                    "Deseja voltar ao Menu?",
                    choices=[
                        "Sim",
                        "Não", ]).ask()
        
                if menures == "Sim":
                    continue
                else:
                    break

            elif escolha =="[4] Abrir Log de erros":
                break

            elif escolha =="[5] Sair":
                break

app = App()

app.Rodar()



#mescontagem = 1 
        #for mes in self.meses:

            #print(f"{Fore.RESET} {mes} : ")

            #self.busca.Mostrar_Receita(mescontagem)

            #self.busca.Mostrar_Despesas(mescontagem)

            #self.busca.Mostrar_Saldo(mescontagem)

            #print(Fore.WHITE+"------------------")
            #mescontagem += 1
        #self.busca.RankSaldos()