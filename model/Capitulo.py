class Capitulo:
    
    def __init__(self, numero_capitulo, link_capitulo, data_postagem):
        self.numero_capitulo = numero_capitulo
        self.link_capitulo = link_capitulo
        self.data_postagem = data_postagem
        
        print("Construindo Capitulo ... {}".format(self))


    def __str__(self):
        return f"Numero Capitulo: {self.numero_capitulo}, Link Capitulo: {self.link_capitulo}, Data Postagem: {self.data_postagem}\n"



    def printCapitulo(self):
        print("Numero: ",self.numero_capitulo," Link: ", self.link_capitulo, " Data Postagem: ", self.data_postagem)