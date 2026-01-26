import csv
import os
import keyboard
from colorama import Fore
import pandas as pd



def Mudar_Numeros(valor):

    return "{:,.2f}".format(valor).replace(',', 'v').replace('.', ',').replace('v', '.')

class Arquivos:

    def VerificarDados(self,dados):

        dadosbons = []

        linhasvazias = 0
        for linha in dados:

            try:
                tranformarnum = float(linha['valor'])

            except ValueError:
                linhasvazias +=1
                continue

            if linha['valor'] == '' :
                linhasvazias +=1

            elif linha['data'] == '' or  "-" not in linha['data'] :
                linhasvazias +=1

        
            else:
                dadosbons.append(linha)

        print(f"{linhasvazias} Linhas vazias ou erradas")

        return dadosbons



    def Abrir_Arquivos(self,):

        caminho = os.path.join(os.path.dirname(__file__), "..", "data")


        dados = []

        for arquivo in os.listdir(caminho):

            with open(rf"{caminho}\{arquivo}",newline="",encoding='utf-8') as csvfile:

                leitor = csv.DictReader(csvfile)

                for linha in leitor:
                    dados.append(linha)

        dadosbons = self.VerificarDados(dados)

        return dadosbons


class Busca:

    def __init__(self,):
        
        self.arquivos = Arquivos()
        self.dados = self.arquivos.Abrir_Arquivos()
        self.meses = [
                'Janeiro', 'Fevereiro', 'Março', 'Abril', 
                'Maio', 'Junho', 'Julho', 'Agosto', 
                'Setembro', 'Outubro', 'Novembro', 'Dezembro'
        ]


    def Mostrar_Saldo (self,nummes):

        valores = []

        for linha in self.dados:

            if int(linha['data'].split("-")[1]) == nummes:

                valores.append(float(linha['valor']))

        soma= sum(valores)

        print(Fore.YELLOW+f"O Saldo do Final do mês foi de: R$ {Mudar_Numeros(soma)}")

    def Mostrar_Receita(self,numes):

        valores = []

        for linha in self.dados :

            if int(linha['data'].split("-")[1]) == numes:

                if float(linha['valor']) > 0:
                    valores.append(float(linha['valor']))
        

        soma= sum(valores)

        print(Fore.GREEN+f"O Valor da Receita do mês foi de: R$ {Mudar_Numeros(soma)}")

    def Mostrar_Despesas(self,numes):

        valores = []

        for linha in self.dados:

            if int(linha['data'].split("-")[1]) == numes:

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

                if int(linha['data'].split("-")[1]) == mescontagem:

                    soma_do_mes.append(float(linha['valor']))
            
            soma_saldo = sum(soma_do_mes)
            mescontagem += 1



            resultados[mes] = soma_saldo

        
        maiorvalor=max(resultados, key=resultados.get)
        
        piorvalor = min(resultados,key=resultados.get)

        
        somaanual = sum(resultados.values())

        print("RESUMO ANUAL :")

        print(f"O mês com o maior saldo foi: {maiorvalor} (R${Mudar_Numeros(resultados[maiorvalor])})")

        print(f"O mês com o pior saldo foi: {piorvalor} (R${Mudar_Numeros(resultados[piorvalor])})")

        print(F"Saldo total do ano: R${Mudar_Numeros(somaanual)}")


class App:


    def __init__(self):
        self.meses = [
                'Janeiro', 'Fevereiro', 'Março', 'Abril', 
                'Maio', 'Junho', 'Julho', 'Agosto', 
                'Setembro', 'Outubro', 'Novembro', 'Dezembro'
        ]

        self.busca = Busca()

    def Rodar(self,):


        mescontagem = 1 
        for mes in self.meses:

            print(f"{Fore.RESET} {mes} : ")

            self.busca.Mostrar_Receita(mescontagem)

            self.busca.Mostrar_Despesas(mescontagem)

            self.busca.Mostrar_Saldo(mescontagem)

            

            print(Fore.WHITE+"------------------")
            mescontagem += 1
        self.busca.RankSaldos()

        keyboard.wait("g")


app = App()

app.Rodar()


