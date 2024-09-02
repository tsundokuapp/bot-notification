import logging

from src.model.obra import Obra
from src.model.capitulo import Capitulo
from src.model.posts.post_discord import PostDiscord
from src.dao.atlas_dao import AtlasDAO

class TestModelPosts:

    def test_instanciacao(self):
        atlas_dao = AtlasDAO()

        #Instanciando o objeto da obra e adicionando capitulos
        obra = Obra("Jirai Nandesuka? Chihara-san", "https://i1.wp.com/tsundoku.com.br/wp-content/uploads/2021/12/Capa-Chihara.jpg", "https://tsundoku.com.br/manga/jirai-nandesuka-chihara-san/")
        lista_capitulos = [
            Capitulo("40", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/", "setembro 4, 2023"),
            Capitulo("41", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-41/", "setembro 4, 2023")
        ]
        obra.receber_lista_de_capitulos(lista_capitulos)

        post_discord = PostDiscord(obra, atlas_dao.receber_obras())

        assert post_discord.titulo_obra == obra.titulo_obra
        assert post_discord.url_obra == obra.url_obra
        assert post_discord.nome_no_anuncio == "Jirai nandesuka? Chihara-san"
        assert post_discord.cor_int == int('0xe4012e', 16)
        assert post_discord.imagem_obra == "https://tsundoku.com.br/wp-content/uploads/2024/07/Banner-Chihara.png"


    def test_tipos_sao_validos(self):
        atlas_dao = AtlasDAO()

        #Instanciando o objeto da obra e adicionando capitulos
        obra = Obra("Jirai Nandesuka? Chihara-san", "https://i1.wp.com/tsundoku.com.br/wp-content/uploads/2021/12/Capa-Chihara.jpg", "https://tsundoku.com.br/manga/jirai-nandesuka-chihara-san/")
        lista_capitulos = [
            Capitulo("40", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/", "setembro 4, 2023"),
            Capitulo("41", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-41/", "setembro 4, 2023")
        ]
        obra.receber_lista_de_capitulos(lista_capitulos)

        post_discord = PostDiscord(obra, atlas_dao.receber_obras())

        assert isinstance(post_discord.titulo_obra, str)
        assert isinstance(post_discord.url_obra, str)
        assert isinstance(post_discord.nome_no_anuncio, str)
        assert isinstance(post_discord.cor_int, int)
        assert isinstance(post_discord.imagem_obra, str)