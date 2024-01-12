import os
import requests
import logging

from src.dao.atlas_dao import AtlasDAO

class DownloadImagens: 

    def fazer_download_imagens_obras():
        atlas_dao = AtlasDAO()

        logger_infos = logging.getLogger('logger_infos')

        # Obter os documentos como uma lista
        dados_lista = atlas_dao.receber_obras()

        diretorio_destino = 'assets/imagens'  # Diretório onde as imagens serão salvas

        # Verifica se o diretório de destino existe, se não, cria-o
        if not os.path.exists(diretorio_destino):
            os.makedirs(diretorio_destino)

        # Itera sobre os documentos na lista
        for documento in dados_lista:
            chave = documento.get('titulo') 
            url_imagem = documento.get('url_imagem')

            if chave and url_imagem:
                nome_arquivo = os.path.join(diretorio_destino, chave + '.png')

                # Verifica se a imagem já existe
                if os.path.exists(nome_arquivo):
                    logger_infos.info(f'Imagem já existe: {nome_arquivo}')
                    continue  # Pula para a próxima iteração

                response = requests.get(url_imagem)
                response.raise_for_status()  # Verifica se ocorreu algum erro durante a solicitação

                with open(nome_arquivo, 'wb') as arquivo:
                    arquivo.write(response.content)

                logger_infos.info(f'Imagem baixada: {nome_arquivo}')
            else:
                logger_infos.info('Documento sem chave ou URL de imagem')
