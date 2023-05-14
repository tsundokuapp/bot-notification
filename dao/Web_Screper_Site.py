from model.Capitulo import Capitulo
from model.Obra import Obra
from model.Mensagens import Mensagens

from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import locale

# Definir o locale como "pt_BR.UTF-8"
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


class Web_Screper_Site:

    def __init__(self):
        print("Iniciando web screper")


    def recebe_capitulos_diarios(self):
        Mensagens.recebendo_capitulos_mensagem()

        lista_de_obras = []

        for numero_atual in [5,6,7,8]:

            dados_obra = self.receber_conteudo(numero_atual)

            titulo_obra = dados_obra[0]
            imagem_obra = dados_obra[3]
            url_obra = dados_obra[4]

            obra = Obra(titulo_obra, imagem_obra, url_obra)
            lista_de_capitulos = self.receber_capitulos_diarios_obras(url_obra)

            if len(lista_de_capitulos) == 0:
                print(f"Nenhum post de {titulo_obra}. \n")
            else:
                obra.receber_lista_de_capitulos(lista_de_capitulos)
                lista_de_obras.append(obra)

        print(lista_de_obras)
        return lista_de_obras

 
    def receber_capitulos_diarios_obras(self, url_obra):
        response = requests.get(url_obra)
        soup = BeautifulSoup(response.text, 'html.parser')

        dados_postagem = soup.find('div', {'class': 'eplister'}).find('ul')

        lista_de_capitulos = []

        datas = []
        for i in range(7):
            data = datetime.now().date() - timedelta(days=i)
            data = data.strftime("%B %-d, %Y")
            datas.append(data)

        for li in dados_postagem.find_all("li"):
            chapterdate = li.find("span", class_="chapterdate").text
            if chapterdate in datas:
                chapternum = li.find("span", class_="chapternum").text
                chapterlink = li.find("a")["href"]
                lista = [chapternum, chapterdate, chapterlink]
                capitulo = Capitulo(lista[0], lista[2], lista[1])
                lista_de_capitulos.append(capitulo) # Adiciona a lista à matriz

        return lista_de_capitulos


    def receber_conteudo(self, numero_partir_ultimo_capitulo_postado):
        url = 'https://tsundoku.com.br'

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        divs_bsx = soup.find_all(name='div', class_='bsx')
        ultima_atualizada = divs_bsx[numero_partir_ultimo_capitulo_postado]

        titulo_obra = ultima_atualizada.select_one('.tt a')['title']
        url_obra = ultima_atualizada.select_one('.tt a')['href']

        url_obra = ultima_atualizada.select_one('.bsx a')['href']
        url_ultimo_capitulo = ultima_atualizada.select_one('.chfiv a')['href']
        
        numero_ultimo_capitulo = ultima_atualizada.select_one('.chfiv a').text

        response = requests.get(url_obra)
        soup = BeautifulSoup(response.text, 'html.parser')
        imagem_obra = soup.select_one('.thumb img')['src']

        dados_ultima_obra_atualizada = [titulo_obra,numero_ultimo_capitulo,url_ultimo_capitulo,imagem_obra,url_obra]

        return dados_ultima_obra_atualizada