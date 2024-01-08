from src.dao.Conexao_Discord import Conexao_Discord
from src.dao.Atlas_Dao import Atlas_DAO
from src.model.Capitulo import Capitulo
from src.model.Obra import Obra
from src.model.posts.Post_Discord import Post_Discord


class TestConexaoDiscord:
    def test_postagem_capitulos_esta_funcionando(self):

        atlas_dao = Atlas_DAO()

        obra = Obra("Teste de Postagem", "https://tsundoku.com.br/wp-content/uploads/2022/02/Gosu_The_Master1.png","https://tsundoku.com.br/manga/liberte-aquela-bruxa/")

        post_discord = Post_Discord(obra, atlas_dao.receber_obras())

        capitulo_um = Capitulo("9998", "https://tsundoku.com.br/liberte-aquela-bruxa-vol-03-cap-349-passagem-parte-1/", "junho 27, 2023")

        capitulo_dois= Capitulo("9999", "https://tsundoku.com.br/liberte-aquela-bruxa-vol-03-cap-345-passagem-parte-2/", "junho 27, 2023")

        post_discord.lista_de_capitulos += [capitulo_um, capitulo_dois]
        post_discord.nome_no_anuncio = "Gosu"

        Conexao_Discord.postar_anuncio_discord(post_discord,True)
        assert True