import logging

class Capitulo:
    
    def __init__(self, numero_capitulo: str, link_capitulo: str, data_postagem: str):
        if (
            not isinstance(numero_capitulo, str) or
            not isinstance(link_capitulo, str) or
            not isinstance(data_postagem, str)
        ):
            raise ValueError("Tipo de dado inválido.")
        
        self._numero_capitulo = numero_capitulo
        self._link_capitulo = link_capitulo
        self._data_postagem = data_postagem
        self.logger_infos = logging.getLogger('logger_infos')


    @property
    def numero_capitulo(self):
        return self._numero_capitulo
    
    
    @property
    def link_capitulo(self):
        return self._link_capitulo
    

    @property
    def data_postagem(self):
        return self._data_postagem


    def __str__(self) -> str:
        return f"Numero Capitulo: {self.numero_capitulo}, Link Capitulo: {self.link_capitulo}, Data Postagem: {self.data_postagem}\n"


    def __repr__(self) -> str:
        return f"Numero Capitulo: {self.numero_capitulo}"


    def printCapitulo(self) -> None:
        print("Numero: ",self.numero_capitulo," Link: ", self.link_capitulo, " Data Postagem: ", self.data_postagem)