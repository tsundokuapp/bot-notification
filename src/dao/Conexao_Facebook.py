import os
from dotenv import load_dotenv
import facebook

class Conexao_Facebook:

    def postar_anuncio_facebook(post_obra):
        def receber_caminho_imagem(titulo_obra):
            diretorio_imagens = "imagens"
            caminho_imagem = os.path.join(diretorio_imagens, f"{titulo_obra}.png")
        
            return caminho_imagem

        load_dotenv()
        token_de_acesso_fb = os.getenv('API_TOKEN_PAGINA')
        id_pagina_fb = os.getenv("API_ID_PAGINA_FACEBOOK")

        graph = facebook.GraphAPI(access_token=token_de_acesso_fb, version="3.0")

        # Faz a postagem
        # graph.put_object(parent_object=id_pagina_fb, connection_name='feed', message=post_obra.retornar_mensagem_post())

        caminho_imagem = receber_caminho_imagem(post_obra.titulo_obra)
        with open(caminho_imagem, 'rb') as imagem:
            graph.put_photo(image=imagem, message=post_obra.retornar_mensagem_post())

        return
