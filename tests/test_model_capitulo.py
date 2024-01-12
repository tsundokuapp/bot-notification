import pytest
from src.model.capitulo import Capitulo

class TestModelCapitulo:
    # Teste de inicialização
    def test_inicializacao(self):
        capitulo = Capitulo("40", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/", "setembro 4, 2023")
        assert capitulo.numero_capitulo == "40"
        assert capitulo.link_capitulo == "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/"
        assert capitulo.data_postagem == "setembro 4, 2023"
        assert isinstance(capitulo.numero_capitulo, str)
        assert isinstance(capitulo.link_capitulo, str)
        assert isinstance(capitulo.data_postagem, str)


    # Teste de tipo de dado inválido
    def test_tipo_dado_invalido(self):
        with pytest.raises(ValueError):
            Capitulo(40, "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/", "setembro 4, 2023")


    # Teste de representação em string
    def test_str_repr(self):
        capitulo = Capitulo("40", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/", "setembro 4, 2023")
        assert str(capitulo) == "Numero Capitulo: 40, Link Capitulo: https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/, Data Postagem: setembro 4, 2023\n"
        assert repr(capitulo) == "Numero Capitulo: 40"


    # Teste do método printCapitulo
    def test_printCapitulo(self, capsys):
        capitulo = Capitulo("40", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/", "setembro 4, 2023")
        capitulo.printCapitulo()
        captured = capsys.readouterr()
        assert captured.out.strip() == "Numero:  40  Link:  https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/  Data Postagem:  setembro 4, 2023"


    # Teste para garantir que a exceção seja levantada com atributos inválidos
    def test_atributos_nao_string(self):
        with pytest.raises(ValueError):
            Capitulo(None, "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/", "setembro 4, 2023")
        with pytest.raises(ValueError):
            Capitulo("40", 12345, "setembro 4, 2023")
        with pytest.raises(ValueError):
            Capitulo("40", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/", 12345)
