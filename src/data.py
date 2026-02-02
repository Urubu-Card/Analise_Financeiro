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


    def Mostrar_Saldo (self,nummes):

        valores = []

        for linha in self.dados:

            data = datatime.strptime(linha['data'],"%Y-%m-%d")

            if data.month == nummes:

                valores.append(float(linha['valor']))

        soma= sum(valores)

        print(Fore.YELLOW+f"O Saldo do Final do mês foi de: R$ {Mudar_Numeros(soma)}")

    def Mostrar_Receita(self,numes):

        valores = []

        for linha in self.dados :

            data = datatime.strptime(linha['data'],"%Y-%m-%d")

            if data.month == numes:

                if float(linha['valor']) > 0:
                    valores.append(float(linha['valor']))
        

        soma= sum(valores)

        #print(Fore.GREEN+f"O Valor da Receita do mês foi de: R$ {Mudar_Numeros(soma)}")
        return Mudar_Numeros(soma)

    def Mostrar_Despesas(self,numes):

        valores = []

        for linha in self.dados:

            data = datatime.strptime(linha['data'],"%Y-%m-%d")

            if data.month == numes:

                if float(linha['valor']) < 0:
                    valores.append(float(linha['valor']))
        

        soma= sum(valores)

        print(Fore.RED+f"O Valor da Despesa do mês foi de: R$ {Mudar_Numeros(soma)}")

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
            'saldo': saldo_mes,
            'receita': receita_mes,
            'despesa': despesa_mes
        })

            valores_tabela_terminal.append([saldo_mes, receita_mes, despesa_mes])

        #df = pd.DataFrame(valores_tabela,columns=labe,index=self.meses)
        return valores_tabela_html, valores_tabela_terminal

