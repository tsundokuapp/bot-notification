from src.dao.atlas_dao import AtlasDAO
from src.model.obra import Obra
from src.model.capitulo import Capitulo
import time

class TestDaoAtlasDao:
    def test_validar_conexao(self):
        atlas_dao = AtlasDAO()

        assert atlas_dao.testar_conexao()
        
    
    def test_valida_consulta_obras_anunciadas(self):
        atlas_dao = AtlasDAO()
        
        try:
           lista_obras = atlas_dao.receber_obras_anunciadas()
           print(lista_obras)
        except Exception as e:
            assert False, f"Erro durante a consulta de obras anunciadas: {e}"

        assert True


    def test_valida_orden_consulta_obras_anunciadas(self):
        atlas_dao = AtlasDAO()

        obra = Obra("Obra de Teste", "Teste", "Teste")
        obra.imagem_obra = "Teste"
        lista_capitulos = [
            Capitulo("42", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-41/", "setembro 4, 2023"),
            Capitulo("45", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-41/", "setembro 4, 2023"),
            Capitulo("44", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-41/", "setembro 4, 2023"),
            Capitulo("41", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-41/", "setembro 4, 2023"),
            Capitulo("42", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-41/", "setembro 4, 2023"),
        ]
        obra.receber_lista_de_capitulos(lista_capitulos)
        
        try:
           atlas_dao.adicionar_obras_anunciadas([obra])

           obra_atualizada = atlas_dao.receber_obra_anunciada_por_titulo(obra.titulo_obra)

           [print(capitulo) for capitulo in obra_atualizada.lista_de_capitulos]

           assert obra_atualizada.lista_de_capitulos[0].numero_capitulo == "45", "A ordenação não foi realizada corretamente."
           assert obra_atualizada.lista_de_capitulos[3].numero_capitulo == "41", "A ordenação não foi realizada corretamente."

           atlas_dao.excluir_registros_de_obra_anunciada_por_titulo(obra)
        
        except Exception as e:
            assert False, f"Erro durante a consulta de obras anunciadas: {e}"

        assert True


    def test_valida_adicao_obras_anunciadas(self):
        atlas_dao = AtlasDAO()

        obra = Obra("Obra de Teste", "Teste", "Teste")
        obra.imagem_obra = "Teste"
        lista_capitulos = [
            Capitulo("40", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-41/", "setembro 4, 2023"),
        ]
        obra.receber_lista_de_capitulos(lista_capitulos)

        try:
            atlas_dao.adicionar_obras_anunciadas([obra])

            obra_atualizada = atlas_dao.receber_obra_anunciada_por_titulo(obra.titulo_obra)

            assert obra_atualizada is not None, "A obra não foi adicionada corretamente."

            atlas_dao.excluir_registros_de_obra_anunciada_por_titulo(obra_atualizada)

        except Exception as e:
            assert False, f"Erro durante a adição de obras anunciadas: {e}"

        assert True
        
    
    def test_valida_exclusao_obra_anunciadas(self):

        atlas_dao = AtlasDAO()

        obra = Obra("Obra de Teste", "Teste", "Teste")
        obra.imagem_obra = "Teste"
        lista_capitulos = [
            Capitulo("40", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-41/", "setembro 4, 2023"),
        ]
        obra.receber_lista_de_capitulos(lista_capitulos)

        atlas_dao.adicionar_obras_anunciadas([obra])

        obra_atualizada = atlas_dao.receber_obra_anunciada_por_titulo(obra.titulo_obra)

        atlas_dao.excluir_registros_de_obra_anunciada_por_titulo(obra_atualizada)

        assert atlas_dao.receber_obra_anunciada_por_titulo(obra.titulo_obra) is None, "A obra não foi excluída corretamente."


    def test_verifica_atualizacao_capitulos_anunciados(self):
        atlas_dao = AtlasDAO()

        obra = Obra("Obra de Teste", "Teste", "Teste")
        obra.imagem_obra = "Teste"
        lista_capitulos = [
            Capitulo("39", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-41/", "setembro 4, 2023")
        ]
        obra.receber_lista_de_capitulos(lista_capitulos)

        atlas_dao.adicionar_obras_anunciadas([obra])

        obra_dois = Obra("Obra de Teste", "Teste", "Teste")
        obra_dois.imagem_obra = "Teste"
        capitulos_adicionais = [
            Capitulo("41", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/", "setembro 4, 2023"),
            Capitulo("40", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-41/", "setembro 4, 2023"),
            Capitulo("42", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-41/", "setembro 4, 2023"),
        ]
        obra_dois.receber_lista_de_capitulos(capitulos_adicionais)

        atlas_dao.adicionar_obras_anunciadas([obra_dois])

        time.sleep(2)

        obra_atualizada = atlas_dao.receber_obra_anunciada_por_titulo(obra.titulo_obra)

        obra.receber_lista_de_capitulos(obra_dois.lista_de_capitulos)

        assert len(obra_atualizada.lista_de_capitulos) == len(obra.lista_de_capitulos), "O número de capítulos não foi atualizado corretamente após a exclusão."

        atlas_dao.excluir_registros_de_obra_anunciada_por_titulo(obra_atualizada)

        time.sleep(2)

        assert atlas_dao.receber_obra_anunciada_por_titulo(obra.titulo_obra) is None

