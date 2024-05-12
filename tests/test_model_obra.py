from src.model.obra import Obra
from src.model.capitulo import Capitulo

class TestModelObra: 
    def test_inicializacao(self):
        obra = Obra("Jirai Nandesuka? Chihara-san", "https://i1.wp.com/tsundoku.com.br/wp-content/uploads/2021/12/Capa-Chihara.jpg", "https://tsundoku.com.br/manga/jirai-nandesuka-chihara-san/")
        assert isinstance(obra.titulo_obra, str)
        assert isinstance(obra.imagem_obra, str)
        assert isinstance(obra.url_obra, str)


    def test_str_repr(self):
        obra = Obra("Jirai Nandesuka? Chihara-san", "https://i1.wp.com/tsundoku.com.br/wp-content/uploads/2021/12/Capa-Chihara.jpg", "https://tsundoku.com.br/manga/jirai-nandesuka-chihara-san/")
        assert str(obra) == "Titulo: Jirai Nandesuka? Chihara-san, Link Imagem: https://i1.wp.com/tsundoku.com.br/wp-content/uploads/2021/12/Capa-Chihara.jpg, Link Obra: https://tsundoku.com.br/manga/jirai-nandesuka-chihara-san/, Caps: [] \n"
        assert repr(obra) == "Titulo: Jirai Nandesuka? Chihara-san"


    def test_adicionar_capitulo(self):
        obra = Obra("Jirai Nandesuka? Chihara-san", "https://i1.wp.com/tsundoku.com.br/wp-content/uploads/2021/12/Capa-Chihara.jpg", "https://tsundoku.com.br/manga/jirai-nandesuka-chihara-san/")
        obra.adicionar_capitulo("40", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/", "setembro 4, 2023")

        assert len(obra.lista_de_capitulos) == 1
        assert isinstance(obra.lista_de_capitulos[0], Capitulo)


    def test_receber_lista_de_capitulos(self):
        obra = Obra("Jirai Nandesuka? Chihara-san", "https://i1.wp.com/tsundoku.com.br/wp-content/uploads/2021/12/Capa-Chihara.jpg", "https://tsundoku.com.br/manga/jirai-nandesuka-chihara-san/")
        lista_capitulos = [
            Capitulo("40", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/", "setembro 4, 2023"),
            Capitulo("41", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-41/", "setembro 4, 2023")
        ]
        obra.receber_lista_de_capitulos(lista_capitulos)
        assert len(obra.lista_de_capitulos) == 2
        # Verifique se os elementos da lista são instâncias de Capitulo
        assert all(isinstance(capitulo, Capitulo) for capitulo in obra.lista_de_capitulos)

    
    def test_obra_conseguiu_ordenar_capitulos(self):
        obra = Obra("Jirai Nandesuka? Chihara-san", "https://i1.wp.com/tsundoku.com.br/wp-content/uploads/2021/12/Capa-Chihara.jpg", "https://tsundoku.com.br/manga/jirai-nandesuka-chihara-san/")
        
        lista_capitulos = [
            Capitulo("39", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-41/", "setembro 4, 2023"),
            Capitulo("41", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-40/", "setembro 4, 2023"),
            Capitulo("40", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-41/", "setembro 4, 2023"),
            Capitulo("42", "https://tsundoku.com.br/jirai-nandesuka-chihara-san-cap-41/", "setembro 4, 2023"),
        ]
        
        obra.receber_lista_de_capitulos(lista_capitulos)
        
        print("Lista Ordenada: " + str(obra.lista_de_capitulos))
        
        # Verifica se a lista está ordenada pelo número do capítulo
        capitulos_ordenados = sorted(lista_capitulos, key=lambda capitulo: int(capitulo.numero_capitulo), reverse=True)
        assert obra.lista_de_capitulos == capitulos_ordenados
