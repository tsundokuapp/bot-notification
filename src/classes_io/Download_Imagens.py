import os
import requests

from src.classes_io.Gestor_JSON import Gestor_JSON

class Download_Imagens: 

    def fazer_download_imagens_obras():

        gestor_json = Gestor_JSON()

        # Percorrer o JSON e baixar as imagens
        dados = gestor_json.retornar_dados_unicos_obras()

        diretorio_destino = 'assets/imagens'  # Diretório onde as imagens serão salvas

        # Verifica se o diretório de destino existe, se não, cria-o
        if not os.path.exists(diretorio_destino):
            os.makedirs(diretorio_destino)

        # Itera sobre os dados e baixa as imagens
        for chave, valor in dados.items():
            url_imagem = valor['url_imagem']
            nome_arquivo = os.path.join(diretorio_destino, chave + '.png')  # Define o nome do arquivo usando a chave do JSON

            # Verifica se a imagem já existe
            if os.path.exists(nome_arquivo):
                print(f'Imagem já existe: {nome_arquivo}')
                continue  # Pula para a próxima iteração

            response = requests.get(url_imagem)
            response.raise_for_status()  # Verifica se ocorreu algum erro durante a solicitação

            with open(nome_arquivo, 'wb') as arquivo:
                arquivo.write(response.content)

            print(f'Imagem baixada: {nome_arquivo}')