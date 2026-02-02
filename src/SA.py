import os
from datetime import datetime as datatime # Fica mais facil de entender 
import csv



def Mudar_Numeros(valor):
    'Arruma os numeros para ficarem com virgula e pontos de direitinho (Ex: 1.000,67).'

    return "{:,.2f}".format(valor).replace(',', 'v').replace('.', ',').replace('v', '.')

class Arquivos:
    'A class que analisa os dados .csv e verifica os dados para nenhum dado corrompido passe.'

    def VerificarDados(self,dados):

        dadosbons = []

        linhasvazias = []
        for num_linha, linha in enumerate(dados, start=1):

            data_str = linha.get('data', '').strip()
            valor_str = linha.get('valor', '').strip()

            #! Verifica se a data ou o valor esta vazio
            if not data_str or not valor_str:
                self.Escreve_Log(f"Linha {num_linha} está com campo vazio: {linha}")
                continue


            #! Verifica se a data ou o valor esta errado
            try:
                data = datatime.strptime(data_str, "%Y-%m-%d")
                valor = float(valor_str)
                
            except ValueError:
                self.Escreve_Log(f"Linha {num_linha} com valor/data inválido: {linha}")
                continue

            dadosbons.append(linha)



        return dadosbons

    def Escreve_Log(self,mensagem):

        if not os.path.exists("logs"):
            os.makedirs("logs")

        caminho_log = os.path.join("logs", "erros.log")

        data_atual = datatime.now().strftime("%d/%m/%Y %H:%M:%S")

        with open(caminho_log, "r+", encoding="utf-8") as arquivo:

            if f"ERRO - {mensagem} " not in arquivo.read():
                arquivo.write(f"ERRO - {mensagem} \n")

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

app = Arquivos()

app.Abrir_Arquivos()