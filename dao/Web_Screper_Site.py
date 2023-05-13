from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

class Web_Screper_Site:

    def __init__(self):
        print("Construindo objeto ... {}".format(self))
        self.matriz_de_capitulos = []

    def recebe_capitulos_diarios(self):
        for numero_atual in [5,6,7,8]:

            dados_obra = self.receber_conteudo(numero_atual)

            titulo_obra = dados_obra[0]
            imagem_obra = dados_obra[3]
            url_obra = dados_obra[4]
            print(url_obra)

            matriz_capitulos = self.receber_capitulos_diarios_sem_filtro(url_obra)
            print(matriz_capitulos)


  #  def receber_capitulos_diarios_sem_filtro(self, url_obra):
        response = requests.get(url_obra)
        soup = BeautifulSoup(response.text, 'html.parser')

        dados_postagem = soup.find('div', {'class': 'eplister'}).find('ul')

        data_atual = datetime.now().strftime("%B %_d, %Y")
        print(data_atual)

        for li in dados_postagem.find_all("li"):
            if li.find("span", class_="chapterdate").text == data_atual:
                chapternum = li.find("span", class_="chapternum").text
                chapterdate = li.find("span", class_="chapterdate").text
                chapterlink = li.find("a")["href"]
                lista = [chapternum, chapterdate, chapterlink]
                self.matriz_de_capitulos.append(lista) # Adiciona a lista à matriz

        # Remove o campo de data da lista
        for lista in self.matriz_de_capitulos:
            del lista[1]

        return self.matriz_de_capitulos


    def receber_capitulos_diarios_sem_filtro(self, url_obra):
        response = requests.get(url_obra)
        soup = BeautifulSoup(response.text, 'html.parser')

        dados_postagem = soup.find('div', {'class': 'eplister'}).find('ul')

        datas = []
        for i in range(3):
            data = datetime.now() - timedelta(days=i)
            datas.append(data.strftime("%B %_d, %Y"))

        print(datas)

        for li in dados_postagem.find_all("li"):
            chapter_date = li.find("span", class_="chapterdate").text.strip()
            if chapter_date in datas:
                chapternum = li.find("span", class_="chapternum").text
                chapterlink = li.find("a")["href"]
                lista = [chapternum, chapter_date, chapterlink]
                print(list)
                self.matriz_de_capitulos.append(lista)


        # Remove o campo de data da lista
        for lista in self.matriz_de_capitulos:
            del lista[1]

        return self.matriz_de_capitulos


    def receber_capitulos_diarios_data_desejada(self, url_obra, data_desejada):
        response = requests.get(url_obra)
        soup = BeautifulSoup(response.text, 'html.parser')

        dados_postagem = soup.find('div', {'class': 'eplister'}).find('ul')

        data_atual = datetime.now().strftime(data_desejada, "%B %_d, %Y")

        matriz_de_capitulos = [] # Inicializa a matriz vazia

        for li in dados_postagem.find_all("li"):
            if li.find("span", class_="chapterdate").text == data_atual:
                chapternum = li.find("span", class_="chapternum").text
                chapterdate = li.find("span", class_="chapterdate").text
                chapterlink = li.find("a")["href"]
                lista = [chapternum, chapterdate, chapterlink]
                matriz_de_capitulos.append(lista) # Adiciona a lista à matriz

        # Remove o campo de data da lista
        for lista in matriz_de_capitulos:
            del lista[1]

        return matriz_de_capitulos


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