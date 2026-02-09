import os
from datetime import datetime as datatime # Fica mais facil de entender 
import csv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


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

        caminho_log = fr"{BASE_DIR}/logs"

        print(caminho_log)
        caminho_arqui = (caminho_log+r"\erros.log")

        if not os.path.exists(caminho_log):
            os.makedirs("logs")

        with open(caminho_arqui, "r+", encoding="utf-8") as arquivo:

            if f"ERRO - {mensagem} " not in arquivo.read():
                arquivo.write(f"ERRO - {mensagem} \n")


    def Abrir_Arquivos(self,):

        caminho = os.path.join(BASE_DIR,"data")


        dados = []

        for arquivo in os.listdir(caminho):

            with open(rf"{caminho}\{arquivo}",newline="",encoding='utf-8') as csvfile:

                leitor = csv.DictReader(csvfile)

                for linha in leitor:
                    dados.append(linha)

        dadosbons = self.VerificarDados(dados)

        return dadosbons


    def Ler_Log(self,):

        log_caminho = os.path.join("logs", "erros.log")

        linhas_error = []

        with open(log_caminho,"r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linhas_error.append(linha)

        return linhas_error

