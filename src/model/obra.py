from src.model.capitulo import Capitulo

class Obra:

    def __init__(self, titulo_obra: str, imagem_obra: str, url_obra: str):
        if (
            not isinstance(titulo_obra, str) or
            not isinstance(imagem_obra, str) or
            not isinstance(url_obra, str)
        ):
            raise ValueError("Tipo de dado inválido.")
        
        self.titulo_obra = titulo_obra
        self.imagem_obra = imagem_obra
        self.url_obra = url_obra

        self.lista_de_capitulos = []
    
    
    def __str__(self):
        return f"Titulo: {self.titulo_obra}, Link Imagem: {self.imagem_obra}, Link Obra: {self.url_obra}, Caps: {self.lista_de_capitulos} \n"


    def __repr__(self):
        return f"Titulo: {self.titulo_obra}"


    def adicionar_capitulo(self, numero_capitulo, link_capitulo, data_postagem) -> None:
        capitulo = Capitulo(numero_capitulo, link_capitulo, data_postagem)
        self.lista_de_capitulos.append(capitulo)

    
    def receber_lista_de_capitulos(self, lista_de_capitulos) -> None:
        # Ordena a lista de capítulos pelo número do capítulo
        lista_ordenada = sorted(lista_de_capitulos, key=lambda capitulo: str(capitulo.numero_capitulo), reverse=True)
        
        self.lista_de_capitulos.extend(lista_ordenada)