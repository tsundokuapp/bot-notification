from model.Capitulo import Capitulo

class Obra:

    def __init__(self, titulo_obra, imagem_obra, url_obra):
        self.titulo_obra = titulo_obra
        self.imagem_obra = imagem_obra
        self.url_obra = url_obra

        self.lista_de_capitulos = []

        print("Construindo Obra ... {}".format(self))

    
    def __str__(self):
        return f"Titulo: {self.titulo_obra}, Link Imagem: {self.imagem_obra}, Link Obra: {self.url_obra} \n"


    def __repr__(self):
        return f"Titulo: {self.titulo_obra}"


    def adicionar_capitulo(self, numero_capitulo, link_capitulo, data_postagem):
        capitulo = capitulo(numero_capitulo, link_capitulo, data_postagem)
        self.lista_de_capitulos.append(capitulo)

    
    def receber_lista_de_capitulos(self, lista_de_capitulos):
        self.lista_de_capitulos = lista_de_capitulos

    
    def teste_poo(self):
        print("Ola mundo")
        

    
    