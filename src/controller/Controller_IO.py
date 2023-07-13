from classes_io.Gestor_JSON import Gestor_JSON
from model.Mensagens import Mensagens

class Controller_IO:

    def valida_existencia_de_anuncios_anteriores():
        Mensagens.inicializando_verificacao_postagem()
        lista_de_obras_recebida = Gestor_JSON.receber_lista_obras_json()

        if len(lista_de_obras_recebida) == 0:
            print("Não existe registro de anúncios!")
            return []
        else:
           return lista_de_obras_recebida