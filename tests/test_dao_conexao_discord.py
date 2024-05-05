from src.dao.conexao_discord import ConexaoDiscord
from src.dao.atlas_dao import AtlasDAO
from src.model.capitulo import Capitulo
from src.model.obra import Obra
from src.model.posts.post_discord import PostDiscord
import pytest

class TestConexaoDiscord:

        
        
    def test_postagem_capitulos_esta_funcionando(self):
        atlas_dao = AtlasDAO()

        obra = Obra("Teste de Postagem", "https://tsundoku.com.br/wp-content/uploads/2022/02/Gosu_The_Master1.png","https://tsundoku.com.br/manga/liberte-aquela-bruxa/")

        post_discord = PostDiscord(obra, atlas_dao.receber_obras())

        capitulo_um = Capitulo("9998", "https://tsundoku.com.br/liberte-aquela-bruxa-vol-03-cap-349-passagem-parte-1/", "junho 27, 2023")

        capitulo_dois= Capitulo("9999", "https://tsundoku.com.br/liberte-aquela-bruxa-vol-03-cap-345-passagem-parte-2/", "junho 27, 2023")

        post_discord.lista_de_capitulos += [capitulo_um, capitulo_dois]
        post_discord.nome_no_anuncio = "teasdasdasd"

        ConexaoDiscord.postar_anuncio_discord(post_discord, True)
