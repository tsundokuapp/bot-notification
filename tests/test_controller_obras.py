from src.controller.controller_obras import ControllerObras
from src.model.obra import Obra
from src.model.capitulo import Capitulo

class TestControllerObras:
    def test_remove_obras_nao_registradas(self):
        # Mock data
        lista_de_obras_recebidas = [
            Obra("Obra Teste 1", "Teste", "Teste"),
            Obra("Obra Teste 2", "Teste", "Teste"),
            Obra("Obra Teste 3", "Teste", "Teste")
        ]
        dados_unicos_obras = [
            {'titulo': 'Obra Teste 1'},
            {'titulo': 'Obra Teste 3'}
        ]

        # Call the function
        obras_registradas = ControllerObras.remove_obras_nao_registradas(lista_de_obras_recebidas, dados_unicos_obras)

        # Assert the results
        assert len(obras_registradas) == 2
        assert obras_registradas[0].titulo_obra == 'Obra Teste 1'
        assert obras_registradas[1].titulo_obra == 'Obra Teste 3'


    def test_remover_obras_que_nao_pode_postar(self):
        # Mock data
        lista_de_obras_para_postar = [
            Obra("Obra Teste 1", "Teste", "Teste"),
            Obra("Obra Teste 2", "Teste", "Teste"),
            Obra("Obra Teste 3", "Teste", "Teste")
        ]
        lista_de_obras_nao_permitidas = [
            {'titulo_obra': 'Obra Teste 2'},
            {'titulo_obra': 'Obra Teste 3'}
        ]

        # Call the function
        obras_filtradas = ControllerObras.remover_obras_que_nao_pode_postar(lista_de_obras_para_postar, lista_de_obras_nao_permitidas)

        # Assert the results
        assert len(obras_filtradas) == 1
        assert obras_filtradas[0].titulo_obra == 'Obra Teste 1'


    def test_valida_lista_obras(self):
        # Mock data
        lista_de_obras = [
            Obra("Obra Teste 1", "Teste", "Teste"),
            Obra("Obra Teste 2", "Teste", "Teste"),
            Obra("Obra Teste 3", "Teste", "Teste")
        ]

        lista_de_obras[0].adicionar_capitulo("40", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/", "setembro 4, 2023")
        lista_de_obras[0].adicionar_capitulo("41", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/", "setembro 4, 2023")
        lista_de_obras[0].adicionar_capitulo("42", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/", "setembro 4, 2023")

        lista_de_obras[2].adicionar_capitulo("01", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/", "setembro 4, 2023")

        lista_de_obras_contidas_no_registro = [
            Obra("Obra Teste 1", "Teste", "Teste"),
            Obra("Obra Teste 2", "Teste", "Teste")
        ]

        lista_de_obras_contidas_no_registro[0].adicionar_capitulo("40", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/", "setembro 4, 2023")
        lista_de_obras_contidas_no_registro[0].adicionar_capitulo("41", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/", "setembro 4, 2023")

        # Call the function
        obras_validadas = ControllerObras.valida_lista_obras(lista_de_obras, lista_de_obras_contidas_no_registro)

        print(obras_validadas)

        # Assert the results
        assert len(obras_validadas) == 2
        assert len(obras_validadas[0].lista_de_capitulos) == 1
        assert obras_validadas[0].lista_de_capitulos.pop().numero_capitulo == '42'
        assert obras_validadas[1].titulo_obra == 'Obra Teste 3'