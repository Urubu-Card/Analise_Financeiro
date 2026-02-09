from colorama import Fore
import pandas as pd
from datetime import datetime as datatime # Fica mais facil de entender 
import SA 


def Mudar_Numeros(valor):
    'Arruma os numeros para ficarem com virgula e pontos de direitinho (Ex: 1.000,67).'

    return "{:,.2f}".format(valor).replace(',', 'v').replace('.', ',').replace('v', '.')


class Busca:

    def __init__(self,):
        
        self.arquivos = SA.Arquivos()
        self.dados = self.arquivos.Abrir_Arquivos()
        self.meses = [
                'Janeiro', 'Fevereiro', 'Março', 'Abril', 
                'Maio', 'Junho', 'Julho', 'Agosto', 
                'Setembro', 'Outubro', 'Novembro', 'Dezembro'
        ]


    def RankSaldos(self):

        resultados = {}

        mescontagem = 1
        for mes in self.meses:

            soma_do_mes = []

            for linha in self.dados:

                data = datatime.strptime(linha['data'],"%Y-%m-%d")

                if data.month == mescontagem:

                    soma_do_mes.append(float(linha['valor']))
            
            soma_saldo = sum(soma_do_mes)
            mescontagem += 1



            resultados[mes] = soma_saldo

        
        maiorvalor=max(resultados, key=resultados.get)
        
        piorvalor = min(resultados,key=resultados.get)

        
        somaanual = sum(resultados.values())

        rank = {"Pior_Valor":   [piorvalor,Mudar_Numeros(resultados[piorvalor])],
                "Maior_Valor":  [maiorvalor,Mudar_Numeros(resultados[maiorvalor])],
                "Soma_Anual":   Mudar_Numeros(somaanual)
                }


        return rank


    def Tabela(self):
        
        labe = ['Saldo',"Receita","Despessas"]

        valores_tabela_html = []

        valores_tabela_terminal = []

        for i in range(1,13):
            saldo_mes = 0
            receita_mes = 0
            despesa_mes = 0

            for linha in self.dados:
                data = datatime.strptime(linha['data'], "%Y-%m-%d")
                
                if data.month == i:
                    valor = float(linha['valor'])
                    saldo_mes += valor
                    if valor > 0:
                        receita_mes += valor
                    else:
                        despesa_mes += valor

            valores_tabela_html.append({
            'mes': self.meses[i-1],
            'saldo': Mudar_Numeros(float(saldo_mes)),
            'receita': Mudar_Numeros(float(receita_mes)),
            'despesa': Mudar_Numeros(float(despesa_mes))
        })

            valores_tabela_terminal.append([saldo_mes, receita_mes, despesa_mes])

        return valores_tabela_html, valores_tabela_terminal
     

class Print_Terminal():

    def __init__(self,):
        self.dados = Busca()


    def Print_Rank(self):
        rank = self.dados.RankSaldos()

        print("RESUMO ANUAL :")

        print(f"O mês com o maior saldo foi:    {rank['Maior_Valor'][0]} (R${rank['Maior_Valor'][1]})")

        print(f"O mês com o pior saldo foi:     {rank['Pior_Valor'][0]} (R${rank['Pior_Valor'][1]})")

        print(F"Saldo total do ano:             R${rank['Soma_Anual']}")


    def Print_Tabela(self):

        labe = ['Saldo',"Receita","Despessas"]

        nao_utilizar , valores_tabela = self.dados.Tabela()

        df = pd.DataFrame(valores_tabela,columns=labe,index=self.dados.meses)

        print(df.map(Mudar_Numeros))
   

    def MostrarLog(self):
        logs = self.dados.arquivos.Ler_Log()

        for log in logs:
            print(log)
