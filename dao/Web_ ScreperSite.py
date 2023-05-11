class recebimento_capitulos_diarios:

    def receber_capitulos_diarios_filtrados(url_obra):
        response = requests.get(url_obra)
        soup = BeautifulSoup(response.text, 'html.parser')

        dados_postagem = soup.find('div', {'class': 'eplister'}).find('ul')

        data_atual = datetime.now().strftime("%B %_d, %Y")

        #ontem = datetime.now() - timedelta(days=1)
        #data_atual = ontem.strftime("%B %_d, %Y")


        print(data_atual)

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

        if len(matriz_de_capitulos) > 3:
            # Adiciona o campo de identificação na lista
            for lista in matriz_de_capitulos:
                lista.append("identificação")
            return [matriz_de_capitulos[0], matriz_de_capitulos[-1]]
        else:
            return matriz_de_capitulos


    def receber_capitulos_diarios_sem_filtro(url_obra):
    response = requests.get(url_obra)
    soup = BeautifulSoup(response.text, 'html.parser')

    dados_postagem = soup.find('div', {'class': 'eplister'}).find('ul')

    data_atual = datetime.now().strftime("%B %_d, %Y")

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


    def receber_conteudo(numero_partir_ultimo_capitulo_postado):
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
