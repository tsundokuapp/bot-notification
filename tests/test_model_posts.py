from src.model.Obra import Obra
from src.model.Capitulo import Capitulo
from src.model.posts.Post_Discord import Post_Discord
from src.dao.Atlas_Dao import Atlas_DAO

class TestModelPosts:

    def test_instanciacao(self):
        atlas_dao = Atlas_DAO()

        #Instanciando o objeto da obra e adicionando capitulos
        obra = Obra("Jirai Nandesuka? Chihara-san", "https://i1.wp.com/tsundoku.com.br/wp-content/uploads/2021/12/Capa-Chihara.jpg", "https://tsundoku.com.br/manga/jirai-nandesuka-chihara-san/")
        lista_capitulos = [
            Capitulo("40", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/", "setembro 4, 2023"),
            Capitulo("41", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-41/", "setembro 4, 2023")
        ]
        obra.receber_lista_de_capitulos(lista_capitulos)

        post_discord = Post_Discord(obra, atlas_dao.receber_obras())

        assert post_discord.titulo_obra == obra.titulo_obra
        assert post_discord.url_obra == obra.url_obra
        assert post_discord.nome_no_anuncio == "Jirai nandesuka? Chihara-san"
        assert post_discord.cor_int == int("0xFFFFFF", 16)
        assert post_discord.imagem_obra == "http://tsundoku.com.br/wp-content/uploads/2022/01/Banner_Chihara_Tsun.png"


    def test_tipos_sao_validos(self):
        atlas_dao = Atlas_DAO()

        #Instanciando o objeto da obra e adicionando capitulos
        obra = Obra("Jirai Nandesuka? Chihara-san", "https://i1.wp.com/tsundoku.com.br/wp-content/uploads/2021/12/Capa-Chihara.jpg", "https://tsundoku.com.br/manga/jirai-nandesuka-chihara-san/")
        lista_capitulos = [
            Capitulo("40", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/", "setembro 4, 2023"),
            Capitulo("41", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-41/", "setembro 4, 2023")
        ]
        obra.receber_lista_de_capitulos(lista_capitulos)

        post_discord = Post_Discord(obra, atlas_dao.receber_obras())

        assert isinstance(post_discord.titulo_obra, str)
        assert isinstance(post_discord.url_obra, str)
        assert isinstance(post_discord.nome_no_anuncio, str)
        assert isinstance(post_discord.cor_int, int)
        assert isinstance(post_discord.imagem_obra, str)


    def test_consegue_encontrar_dados_obra_no_registro(self):
        #Instancia da classe de conexão com banco de dados
        atlas_dao = Atlas_DAO()

        #Instanciando o objeto da obra e adicionando capitulos
        obra = Obra("Jirai Nandesuka? Chihara-san", "https://i1.wp.com/tsundoku.com.br/wp-content/uploads/2021/12/Capa-Chihara.jpg", "https://tsundoku.com.br/manga/jirai-nandesuka-chihara-san/")
        lista_capitulos = [
            Capitulo("40", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/", "setembro 4, 2023"),
            Capitulo("41", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-41/", "setembro 4, 2023")
        ]
        obra.receber_lista_de_capitulos(lista_capitulos)

        post_discord = Post_Discord(obra, atlas_dao.receber_obras())

        logger_infos = logging.getLogger('logger_infos')
        logger_infos.info("Post:")
        logger_infos.info(post_discord.nome_no_anuncio, post_discord.cor_int, post_discord.imagem_obra)

        assert post_discord.nome_no_anuncio == "Jirai nandesuka? Chihara-san"
        assert post_discord.cor_int == int("0xFFFFFF", 16)
        assert post_discord.imagem_obra == "http://tsundoku.com.br/wp-content/uploads/2022/01/Banner_Chihara_Tsun.png"